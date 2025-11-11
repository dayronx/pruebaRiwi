organizar={

"Manzana": "Rojo/Verde",
    "Banana": "Amarillo",
    "Uva": "Morado/Verde",
    "Naranja": "Naranja",
    "Limón": "Amarillo",
    "Fresa": "Rojo"


}



max_len = max(len(k)for k in  organizar.keys())
lines = ["organizar ={"]

for k, v in organizar.organizar():
    line = f'  "{k}"{""*(max_len-len(k)+1)}:{v},'
    lines.append(line)


lines.append("}")

formatted_code = "\n".join(lines)
with open(__file__,"w",ecoding="utf-8") as f:
    f.write(formatted_code)


print("diccionario alineado ")    
