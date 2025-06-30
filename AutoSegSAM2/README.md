# Automated Face & Hand Segmentation using SAM2

## Objective
Detect faces & hands and segment them using SAM2 from Meta via Replicate API.

## Setup
```bash
pip install -r requirements.txt
```

## Environment Variables
Create `.env` file:
```
REPLICATE_API_TOKEN=your_token
```

## Run
```bash
python main.py
```

## Streamlit UI
```bash
streamlit run ui/app.py
```

## Output
Check `output.png` after running.
