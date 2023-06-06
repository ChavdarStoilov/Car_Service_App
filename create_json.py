
result = []

models = {
      "model": "service_app.TestCarsBrands",
      "pk": 1,
      "fields": {
        "brand": 1,
        "model": [],
      }
    }

for id in range(1, 100):
    
    model = input("Enter model: ")
    
    if model == "exit":
        break
    
    
    
    models["fields"]['model'].append((model, ))
#     print(the_model)

# result.append(models)

print(models)


# А1
# A2
# A3
# A4
# A5
# A6
# A7
# A8
# S1
# S2
# S3
# S4
# S5
# S6
# S7
# S8
# Q3
# Q5
# Q7
# Q8