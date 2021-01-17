source venv/bin/activate

echo "Running Intensity Extraction..."
python3 JF_Intensity_Extractor.py

echo "Finding Peaks..."
python3 JF_Peak_Finder.py
