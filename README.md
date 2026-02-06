# All Experiments - LLM‑Based Conversational Modeling of BPMN Collaboration Diagrams with Data

This repository contains all experiments and datasets for the thesis research on LLM‑Based Conversational Modeling of BPMN Collaboration Diagrams with Data.

## Structure

```
.
├── dataset/                    # Datasets used in experiments
│   ├── clustering/            # Clustering analysis and results
│   ├── dataset-all-texts/    # Complete set of textual process descriptions
│   └── dataset-sample-texts/ # Sample texts for experiments 1-4
├── experiments/               # All experimental code and results
│   ├── ex1/                  # Experiment 1: JSON validation and syntax compliance
│   ├── exp2-3/               # Experiments 2-3: Semantic precision, recall, and similarity analysis
│   ├── exp4/                 # Experiment 4: User study and latency analysis
│   └── exp5/                 # Experiment 5: Autofix success rate analysis
└── sample-runs/              # BPMN files and execution outputs
```

## Experiments Overview

### Experiment 1 
**Purpose**: JSON validation and syntax compliance analysis

- Validates BPMN JSON files against a schema
- Analyzes syntax compliance statistics
- **Files**:
  - `get-valid-json-stats.py`: Script to validate JSON files and generate statistics
  - `schema.json`: JSON schema for validation
  - `syntax-compliance.xlsx`: Results of syntax compliance analysis

### Experiments 2-3 
**Purpose**: Semantic precision, recall, and similarity metrics analysis

- **Files**:
  - `percision-recall-similarity.xlsx`: Main results file
  - `percision-recall-similarity - data.xlsx`: Data Objects data
  - `percision-recall-similarity - pools.xlsx`: Pool data

### Experiment 4 
**Purpose**: User study and latency analysis


- **Files**:
  - `analyze.ipynb`: Jupyter notebook for analysis
  - `time.py`: Latency measurement script
  - `surveys.pdf`: Survey questions
  - `*.csv`: Filtered assessment and task data
  - `PU.png`, `PU2.png`: Visualization outputs

### Experiment 5 
**Purpose**: Autofix success rate analysis

- **Files**:
  - `exp5.py`: Main analysis script for autofix success rates
  - `exp5-autofix-success-rate.xlsx`: Results spreadsheet
  - `initial-generation/`: BPMN models before autofix
  - `autofix-applied/`: BPMN models after autofix



## Dataset Structure
- `dataset-all-texts/`: Complete collection of textual process descriptions (PDF and TXT formats)
- `dataset-sample-texts/`: Sample subset for experiments 1-4
- `clustering/`: Clustering analysis results and notebooks


## License

This repository contains research materials for academic purposes.
