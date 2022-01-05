from flask import Flask,render_template
import requests
app = Flask('app')

@app.route('/') 
def hello_world():
	r=requests.get("https://api.clickup.com/api/v2/list/122248309/task?include_closed=true", headers={"Authorization":"pk_10656118_R3Z6SCF4NFGT3H79LPMJRFS40PHLATCR"})
	data = r.json()
	tasks = data["tasks"]
	string = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet"><table style="border: 1px solid black;overflow-wrap: break-word;font-family: 'Rubik', sans-serif;font-size: 24px;">
<link rel="shortcut icon" type="image/icon" href="image.ico">
  <tr>
    <th>Name</th>
		<th>Status</th>
		<th>Class</th>
		<th>Type</th>
		<th>Description</th>
  </tr>
<script>document.title="TASKS";


</script>
  """
	for i in range(len(tasks)):
		#print(tasks[i])
		string = string + """
		
    <tr style="border: 1px solid black;"><td style="border: 1px solid black;width:300px">""" + tasks[i]["name"] + """</td><td style="border: 1px solid black;background-color: """ + tasks[i]["status"]["color"] + """">""" + tasks[i]["status"]["status"] + """</td><td style="border: 1px solid black;background-color: """ + tasks[i]["custom_fields"][0]["type_config"]["options"][int(tasks[i]["custom_fields"][0]["value"])-1]["color"] + """">""" +tasks[i]["custom_fields"][0]["type_config"]["options"][tasks[i]["custom_fields"][0]["value"]]["name"]+"""
</td><td style="border: 1px solid black;background-color: """ + tasks[i]["custom_fields"][2]["type_config"]["options"][int(tasks[i]["custom_fields"][2]["value"])]["color"] + """">""" +tasks[i]["custom_fields"][2]["type_config"]["options"][tasks[i]["custom_fields"][2]["value"]]["name"]+"""</td><td style="border: 1px solid black;width: 400px">""" +str(tasks[i]["description"])+"""</td> </tr>
    
  
		"""
	
	return string + """
  
</table>"""

app.run(host='0.0.0.0', port=8080)