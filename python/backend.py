def backend(event, context):
  print event
  return event['data']
