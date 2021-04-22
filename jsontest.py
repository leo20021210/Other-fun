import json
data='''
{
"family":{
"1":"Toby",
"12":"Tony"
},
"friends":[
{
"name":"Anakin",
"age":28},
{
"name":"Obiwan",
"age":38},
{
"name":"Rex",
"age":48}
],
"name":"Leo",
"age":18
}
'''
info=json.loads(data)
print(info["age"])
print(info["family"]["12"])
lst=info["friends"]
print(len(lst))
for item in lst:
    print(item["name"])
    print(item["age"])

data='''{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}'''
info=json.loads(data)
print(info)
