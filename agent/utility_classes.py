"""Utility classes."""

from typing import TypeVar

from google.cloud.aiplatform import vertexai
import tenacity
from vertexai.generative_models import GenerationConfig
from vertexai.generative_models import GenerativeModel
from vertexai.vision_models import ImageGenerationModel


T = TypeVar('T')

# Vertex AI model ids
# https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference
DEFAULT_T2I_VERTEX_ID = 'imagen-3.0-generate-001'
DEFAULT_LLM_VERTEX_ID = 'gemini-1.5-pro-002'

vertexai.init(project=<YOUR_PROJECT_ID>, location='us-central1') # add your project ID

class LLM:
  """LLM for text manipulation."""

  def __init__(
      self,
      model_id=DEFAULT_LLM_VERTEX_ID,
      use_json_constraints=False,
  ):
    self._client = GenerativeModel(model_id)

    self.use_json_constraints = use_json_constraints

  def generate(self, prompt) -> str:
    """Generates the response from the LLM."""
    if not self.use_json_constraints:
      return self._client.generate_content(prompt).text
    else:
      return self._client.generate_content(
          prompt,
          generation_config=GenerationConfig(
              response_mime_type='application/json'
          ),
      ).text


class ImageGenerator:
  """Generates images from a prompt."""

  def __init__(self, model_url=DEFAULT_T2I_VERTEX_ID):
    self.model_url = model_url
    self.t2i_client = ImageGenerationModel.from_pretrained(model_url)

  @tenacity.retry
  def generate_image(self, conversation: str, seed: int):
    """Generate response from the softres model given conversation."""
    return self.t2i_client.generate_images(
        prompt=conversation,
        # Optional parameters
        number_of_images=1,
        language='en',
        negative_prompt=(
            'multiple dishes, blurry, painting, cartoon, artificial, nsfw, bad'
            ' quality, bad anatomy, worst quality, low quality, low'
            ' resolutions, extra fingers, blur, blurry, ugly, wrongs'
            ' proportions, watermark, image artifacts, lowres, ugly, jpeg'
            ' artifacts, deformed, noisy image'
        ),
        seed=seed,
        add_watermark=False,
        aspect_ratio='1:1',
        safety_filter_level='block_few',
        person_generation='allow_adult',
    )[0]

  def generate_diverse_images(self, conversation: str, seed: int):
    """Samples 4 responses in parallel with different seeds."""
    return self.t2i_client.generate_images(
        prompt=conversation,
        # Optional parameters
        number_of_images=4,
        language='en',
        negative_prompt=(
            'multiple dishes, blurry, painting, cartoon, artificial, nsfw, bad'
            ' quality, bad anatomy, worst quality, low quality, low'
            ' resolutions, extra fingers, blur, blurry, ugly, wrongs'
            ' proportions, watermark, image artifacts, lowres, ugly, jpeg'
            ' artifacts, deformed, noisy image'
        ),
        seed=seed,
        add_watermark=False,
        aspect_ratio='1:1',
        safety_filter_level='block_few',
        person_generation='allow_adult',
    ).images
