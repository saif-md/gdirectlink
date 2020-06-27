from browser import document, alert, window

def linkGenerator(event):
  readLink = document['readLink'].value
  
  if readLink.find('/d/')==-1:
  	document['downloadLink'].text = "Error: Invalid URL"
  else:
  	document['downloadLink'].text = "https://drive.google.com/uc?export=download&id=" + readLink[(readLink.find('/d/')+3):readLink.find('/view')]

document['submitButton'].bind('click', linkGenerator)

def copy(event):
  textElement = document['downloadLink']
  textElement.select()
  document.execCommand('copy')
  
document['copyText'].bind('click', copy)