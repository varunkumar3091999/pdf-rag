def detect_file_type(filepath):
  if filepath.endswith('.pdf'):
    return 'pdf'
  elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
    return 'excel'
  else:
    raise ValueError("Unsupported File")
    
    