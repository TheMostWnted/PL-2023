import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

csv_to_json('alunos.csv', 'alunos.json')




def csv_to_json1(filename):
    data = []
    with open(filename, 'r') as f:
        
        next(f)
        for line in f:
            
            parts = line.strip().split(',')
           
            notas = [int(nota) for nota in parts[3:] if nota]
            
            student = { 'Número' : parts[0],'Nome': parts[1],'Curso': parts[2],'Notas': notas,}
            
            data.append(student)

   
    with open('alunos2.json', 'w') as f:
        json.dump(data, f, indent=2)

    print('JSON file generated successfully!')

csv_to_json1("alunos2.csv")

with open('alunos2.json', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content.encode('utf-8').decode('unicode_escape'))



def csv_to_json2(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        data = []
        for row in reader:
            
            notas = []
            for i in range(3, 6):
                nota = row.get(f'Notas{{{i}}}')
                if nota:
                    notas.extend(nota.split(','))
            notas = [int(nota) for nota in notas]

            
            row_dict = {}
            for header in headers:
                if header == 'Notas{3,5}':
                    row_dict['Notas'] = notas
                else:
                    row_dict[header] = row.get(header)

            data.append(row_dict)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

csv_to_json2("alunos3.csv","alunos3.json")



def csv_to_json3(csv_file, json_file):
    
    with open(csv_file, 'r') as f:
        
        reader = csv.reader(f)
        
        header = next(reader)
        
        sum_columns = [i for i, c in enumerate(header) if '::sum' in c]
        
        column_names = [c.replace('::sum', '') for c in header if '::sum' not in c]
        
        data = []
        
        for row in reader:
           
            number, name, course = row[:3]
           
            sum_values = [sum(map(int, row[i].split(','))) if i in sum_columns else 0 for i in range(3, len(row))]
            
            student_data = dict(zip(column_names, sum_values))
            student_data['Número'] = number
            student_data['Nome'] = name
            student_data['Curso'] = course
            
            data.append(student_data)
   
    with open(json_file, 'w') as f:
        
        json.dump(data, f)


csv_to_json3('alunos4.csv', 'alunos4.json')


def csv_to_json4(csv_file, json_file):
  
    with open(csv_file, 'r') as f:
        
        reader = csv.reader(f)
        
        header = next(reader)
        
        avg_columns = [i for i, c in enumerate(header) if '::media' in c]
        
        column_names = [c.replace('::media', '') for c in header if '::media' not in c]
        
        data = []
        
        for row in reader:
            
            number, name, course = row[:3]
            
            avg_values = [sum(map(int, row[i].split(','))) / len(row[i].split(',')) if i in avg_columns else 0 for i in range(3, len(row))]
            
            student_data = dict(zip(column_names, avg_values))
            student_data['Número'] = number
            student_data['Nome'] = name
            student_data['Curso'] = course
            
            data.append(student_data)
    
    with open(json_file, 'w') as f:
        
        json.dump(data, f)

csv_to_json4("alunos5.csv","alunos5.json")
