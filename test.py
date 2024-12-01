todos = [
    {
        "id" : 2,
        "label" : "jordy",
        "done" : False,
    },
    {
        "id" : 3 ,
        "label" : "makina",
        "done" : True,
        "descripcion" : "Mamado y retirado",
    }]

new = {

}

for index, unit in enumerate(todos):
    if index == 1:
        for key in unit.keys():
            new[key] = unit[key]
            



print(new)
