from .interface.ISentenceCheck import ISentenceCheck
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import language_tool_python
import torch
import nltk

nltk.download('punkt')

class SentenceCheck(ISentenceCheck):
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"[SentenceCheck] Using device: {self.device}")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2").to(self.device)
        self.tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

    def is_grammatically_correct(self, text):
        matches = self.tool.check(text)
        return len(matches) == 0

    def is_single_word_sentence(self, text):
        return "nosentence" if len(text.split()) <= 1 else text

    def looks_meaningful(self, text):
        words = nltk.word_tokenize(text)
        english_words = [word for word in words if word.isalpha()]
        return len(english_words) / len(words) > 0.5

    def get_perplexity(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs, labels=inputs["input_ids"])
            loss = outputs.loss
        return torch.exp(loss).item()

    def IsSentenceCorrect(self, question: str) -> bool:
        if self.is_single_word_sentence(question) == "nosentence":
            return False
        if not self.looks_meaningful(question):
            return False
        if not self.is_grammatically_correct(question):
            return False
        if self.get_perplexity(question) > 80:
            return False
        if len(question.split()) < 4 or len(question.split()) > 20:
            return False
        if not question.strip().endswith("?"):
            return False
        if question.split()[0].lower() not in [
            "what", "how", "why", "when", "where", "is", "are", "can",
            "should", "could", "who", "does", "do"
        ]:
            return False
        return True
