import os
import json
import subprocess

input_directory = "./raw"
output_directory = "./filtered"

# Überprüfe, ob das Verzeichnis existiert
if os.path.exists(input_directory) and os.path.isdir(input_directory):
    files = os.listdir(input_directory)
    
    # Filtere nur die Dateien, keine Unterverzeichnisse
    files = [f for f in files if os.path.isfile(os.path.join(input_directory, f))]
    
    # Print files
    print("Dateien im Verzeichnis '{}':".format(input_directory))
    print(files)
    
    for file in files:
        print(f"Filtere {file}")
        basisname, dateiendung = os.path.splitext(file)
        output_filename = f"{basisname}_ground{dateiendung}"

        pdal_pipeline = {
            "pipeline": [
                f"{input_directory}/{file}",
                {
                    "type": "filters.smrf",
                    "scalar": 1.2,
                    "slope": 0.2,
                    "threshold": 0.45,
                    "window": 16.0
                },
                {
                    "type": "filters.range",
                    "limits": "Classification[2:2]"
                },
                f"{output_directory}/{output_filename}"
            ]
        }

        pipeline_json = json.dumps(pdal_pipeline)
        command = f'pdal pipeline --stdin <<< \'{pipeline_json}\''
        subprocess.run(command, shell=True, executable='../bin/bash')
                
else:
    print("Das Verzeichnis '{}' existiert nicht oder ist nicht zugänglich.".format(input_directory))