from openai import OpenAI
import os

class LLMClient:
  CATEGORY = "MarkItDown"
  RETURN_TYPES = ("LLM_CLIENT",)
  RETURN_NAMES = ("llm_client",)
  FUNCTION = "execute"
  
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "base_url": ("STRING", {"default": os.environ.get("DEFAULT_LLM_BASE_URL", "")}),
        "api_key": ("STRING", {"default": os.environ.get("DEFAULT_LLM_API_KEY", "")}),
        "model": ("STRING", {"default": os.environ.get("DEFAULT_LLM_MODEL", "")}),
        "prompt": ("STRING", {"default": "Write a detailed description for this image.", "multiline": True}),
      }
    }
    
  def execute(self, base_url, api_key, model, prompt):
    client = OpenAI(base_url=base_url, api_key=api_key)
    client.model = model
    client.prompt = prompt
    return (client,)
    
NODE_CLASS_MAPPINGS = {
  "WIZ_LLM_CLIENT": LLMClient,
}    

NODE_DISPLAY_NAME_MAPPINGS = {
  "WIZ_LLM_CLIENT": "LLM Client",
}