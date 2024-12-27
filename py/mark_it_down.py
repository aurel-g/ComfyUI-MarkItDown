import os
from markitdown import MarkItDown as _MarkItDown

class MarkItDown:
  CATEGORY = "MarkItDown"
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("markdown",)
  FUNCTION = "execute"
  
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "source_file": ("STRING", {}),
      },
    }
      
  def __init__(self):
    self.supported_exts = None
      
  def validate_file_format(self, source_file):  
    if self.supported_exts is not None:
      _, ext = os.path.splitext(source_file)
      if ext.lower() not in self.supported_exts:
        raise ValueError(f"Only support: {self.supported_exts}")
    
  def execute(self, source_file):    
    self.validate_file_format(source_file)
    
    md = _MarkItDown()
    ret = md.convert(source_file)
    txt = ret.text_content
    return (txt,)               

class PDF2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.pdf']

class Word2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.docx']
    
class PowerPoint2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.pptx']

class Excel2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.xlsx']
    
class HTML2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.html', '.htm']    

class Ipynb2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.ipynb']

class Audio2Markdown(MarkItDown):       
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.wav', '.mp3']
    
class Image2Markdown(MarkItDown):
  @classmethod
  def INPUT_TYPES(s):
    its = super().INPUT_TYPES()
    its.update({
      "required": {
        "source_file": ("STRING", {"default": r"D:\work\industry\ai\work\ComfyUI-MarkItDown\data\test.jpg"}),
        "llm_client": ("LLM_CLIENT", {}),
      }      
    }) 
    return its
    
  def __init__(self):
    super().__init__()
    self.supported_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg']
         
  def execute(self, source_file, llm_client):
    self.validate_file_format(source_file)
    llm_model, llm_prompt = llm_client.model, llm_client.prompt
    md = _MarkItDown(llm_client=llm_client, llm_model=llm_model)
    ret = md.convert(source_file, llm_prompt=llm_prompt)
    txt = ret.text_content
    return (txt,)
      
    
NODE_CLASS_MAPPINGS = {
  "WIZ_MARKITDOWN": MarkItDown,
  "WIZ_PDF2MARKDOWN": PDF2Markdown,
  "WIZ_WORD2MARKDOWN": Word2Markdown,
  "WIZ_POWERPOINT2MARKDOWN": PowerPoint2Markdown,
  "WIZ_EXCEL2MARKDOWN": Excel2Markdown,
  "WIZ_HTML2MARKDOWN": HTML2Markdown,
  "WIZ_IPYNB2MARKDOWN": Ipynb2Markdown,
  "WIZ_AUDIO2MARKDOWN": Audio2Markdown,
  "WIZ_IMAGE2MARKDOWN": Image2Markdown,
}    

NODE_DISPLAY_NAME_MAPPINGS = {
  "WIZ_MARKITDOWN": "Mark It Down",
  "WIZ_PDF2MARKDOWN": "PDF to Markdown",
  "WIZ_WORD2MARKDOWN": "Word to Markdown",
  "WIZ_POWERPOINT2MARKDOWN": "PowerPoint to Markdown",
  "WIZ_EXCEL2MARKDOWN": "Excel to Markdown",
  "WIZ_HTML2MARKDOWN": "HTML to Markdown",
  "WIZ_IPYNB2MARKDOWN": "Ipynb to Markdown",
  "WIZ_AUDIO2MARKDOWN": "Audio to Markdown",
  "WIZ_IMAGE2MARKDOWN": "Image to Markdown",
}