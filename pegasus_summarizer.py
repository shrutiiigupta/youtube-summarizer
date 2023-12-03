from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline

# def pegasus_summarizer():
# Pick model
model_name = "google/pegasus-xsum"

# Load pretrained tokenizer
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

example_text = open('transcript.txt').read()

# Define PEGASUS model
# pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Create tokens
# tokens = pegasus_tokenizer(example_text, truncation=True, max_length=7870, padding="max_length")

# Define summarization pipeline
summarizer = pipeline(
    "summarization",
    model=model_name,
    tokenizer=pegasus_tokenizer
)
    # framework="pt"

# summary = summarizer(example_text,truncation=True)
# summary = summarizer(example_text, min_length=200, max_length=1000,truncation=True)
# summary = summarizer(example_text, min_length=200, max_length=1000)
summary = summarizer(example_text)
result=summary[0]["summary_text"]
print(result)
# return(result)

