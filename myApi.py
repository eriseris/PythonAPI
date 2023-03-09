import requests
import json
import os.path

response_API = requests.get('https://api2.dev.dsoftonline.com.au/do/menu-v3/doordash/616')
 
if (response_API.status_code == 200):
     data = response_API.text
     parse_json = json.loads(data)

     payload = {}
     menus = []
     category = []
     items = []
     #sub
     entities = []

     #Menu
     for elem in parse_json['menus']:
          catid = elem['menu']['menu_id']
          gmtitle = elem['menu']['menu_set_name']
          gmsubt = elem['menu']['menu_description_text_footer']
          
     mid = '2023'   
     gmtitle = parse_json['menu_set']['menu_set_name']
     mavial = parse_json['menu_set']['active_days']
  
     menus.append({
          "id":mid,
          "title": {
               "en" : gmtitle
          },
          "subtitle":{
               "en" : gmsubt
          },
          "service_availability":mavial,
          "category_ids" : catid
          })
     
     #Category
     for elem in parse_json['menus']:
          category.append({
               "id" : elem['menu']['menu_id'],
               "title" : {
                    "en" : elem['menu']['menu_title']
               },
               "subtitle" : {
                    "en" : elem['menu']['menu_description_text_header']
               },
               "entities" : entities
          })

     #Items

     for elem in parse_json['menus'][0]['menu_items']:
          
          centsStr = elem['SellShop']
          converted = float(centsStr) * 100

          items.append({
               "id" : elem['PLU'],
               "external_data" : elem['PLU'],
               "title" : {
                    "en" : elem['description']
               },
               "description" : {
                    "en" : "sample description"
               },
               "image_url" : elem['s3_media_url'],
               "price_info": {     
                    "price" : round(converted)
               }
          })
          entities.append({
               "id" : elem['PLU'],
               "type": "ITEM"
          })

     payload.update({
          "menus" : menus,
          "categories" : category,
          "items" : items
     })

     file = os.path.exists('menu.json')

     if file  == True:
          with open('menu.json', 'w') as out_file:
               out_file.write(json.dumps(payload, indent=4))
               print("UpdateComplete")
     else:
          f = open("myfile.txt", "x")
          print("File is created")
          with open('menu.json', 'w') as out_file:
               out_file.write(json.dumps(payload, indent=4))
               print("UpdateComplete")
     
elif (response_API.status_code == 404):
    print("Result not found!")
   


