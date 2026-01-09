import pathway as pw

# Load long novel text using Pathway pipeline
novel_data = pw.io.read_text("data/sample_dataset.txt")

# Optional processing stage
processed = novel_data.map(lambda x: x.lower())

# Run pipeline
try:
    pw.run()
    print("Pathway pipeline executed successfully ✔️")
except Exception as e:
    print("Pipeline Error:", e)
