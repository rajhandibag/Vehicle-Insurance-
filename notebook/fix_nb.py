import json

with open('exp-notebook.ipynb', 'r', encoding='utf-8') as f:
    d = json.load(f)

for c in d['cells']:
    if c['cell_type'] == 'code':
        for i, line in enumerate(c['source']):
            if 'my_params = {' in line:
                c['source'][i] = line.replace(
                    "{'n_estimators': 300, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_depth': 10, 'criterion': 'entropy'}",
                    "{'n_estimators': [300], 'min_samples_split': [7], 'min_samples_leaf': [6], 'max_depth': [10], 'criterion': ['entropy']}"
                )

with open('exp-notebook.ipynb', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=1)
