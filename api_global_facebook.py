import urllib2, json
 
data = urllib2.urlopen('https://graph.facebook.com/EncuentraTuPractica').read()
json_data = json.loads(data)
 
print ('a tu usuario %s le gusta a %s persona!') % (json_data['name'], json_data['likes'])
