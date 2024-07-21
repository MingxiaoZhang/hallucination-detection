# hallucination-detection

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/MingxiaoZhang/hallucination-detection.git
cd hallucination-detection
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application using the command line interface

**Use standard input**

```bash
python main.py
```

**Use file input**

Create `<file_name>.json` file in folder `/test` with format 

```json
{
    "ground_truth": "<your_ground_truth>",
    "llm_output": "<your_llm_output>",
}
```

```bash
python main.py --file test/<file_name>.json
```

## Examples

### Strong semantic relationship

**Input**
```json
{
    "ground_truth": "Recent progress in battery technology includes the creation of solid-state batteries, which provide higher energy density and enhanced safety compared to conventional lithium-ion batteries. Companies such as QuantumScape and Solid Power are at the forefront of these developments, aiming to boost the performance of electric vehicles and portable devices. Furthermore, researchers are investigating silicon anodes to increase battery capacity and graphene-based materials to enhance conductivity and decrease charging times.",
    "llm_output": "Recent advancements in battery technology include the development of solid-state batteries, which offer higher energy density and improved safety compared to traditional lithium-ion batteries. Companies like QuantumScape and Solid Power are making significant progress in this area, aiming to enhance the performance of electric vehicles and portable electronics."
}
```

**Output**
```
Word similarity:  0.9488241672515869
Sentence similarity:  0.8823633193969727
Overall similarity: 0.9023015737533568
Semantic relationship: Strong
```

### Neutral semantic relationship

**Input**
```json
{
    "ground_truth": "Recent progress in battery technology includes the creation of solid-state batteries, which provide higher energy density and enhanced safety compared to conventional lithium-ion batteries. Companies such as QuantumScape and Solid Power are at the forefront of these developments, aiming to boost the performance of electric vehicles and portable devices. Furthermore, researchers are investigating silicon anodes to increase battery capacity and graphene-based materials to enhance conductivity and decrease charging times.",
    "llm_output": "Recent advancements in battery technology include the creation of 'quantum batteries' that use entangled particles to store and release energy instantly. These batteries were recently introduced by a startup called QuantumFuture, and they promise to power devices for decades without any need for recharging."
}
```

**Output**
```
Word similarity:  0.8467316627502441
Sentence similarity:  0.520760715007782
Overall similarity: 0.6185519993305206
Semantic relationship: Neutral
```

### Weak semantic relationship

**Input**
```json
{
    "ground_truth": "Recent advancements in battery technology include the development of solid-state batteries, which offer higher energy density and improved safety compared to traditional lithium-ion batteries. Companies like QuantumScape and Solid Power are making significant progress in this area, aiming to enhance the performance of electric vehicles and portable electronics.",
    "llm_output": "Recent failures in ancient technology include the discovery of a new species of dinosaur in the Gobi Desert. This dinosaur, named 'Electrosaurus,' is believed to have had the ability to generate and store electricity in its body, providing a new insight into the evolutionary biology of prehistoric creatures."
}
```

**Output**
```
Word similarity:  0.7314494848251343
Sentence similarity:  0.305606484413147
Overall similarity: 0.43335938453674316
Semantic relationship: Weak
```
