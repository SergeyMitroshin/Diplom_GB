from peft import PeftModel
from transformers import LLaMATokenizer, LLaMAForCausalLM, GenerationConfig



def generate_prompt(instruction, input=None):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""
    

def llminit():
    tokenizer = LLaMATokenizer.from_pretrained("decapoda-research/llama-7b-hf")
    model = LLaMAForCausalLM.from_pretrained(
      "decapoda-research/llama-7b-hf",
      load_in_8bit=True,
      device_map="auto",
    )
    model = PeftModel.from_pretrained(model, "tloen/alpaca-lora-7b")

    generation_config = GenerationConfig(
    temperature=0.1,
    top_p=0.75,
    num_beams=4,
    )

def evaluate_dummy(instruction, input=None):
    return("Ответ от нейросети")

def evaluate(instruction, input=None):
    prompt = generate_prompt(instruction, input)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].cuda()
    generation_output = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=256
    )
    for s in generation_output.sequences:
        output = tokenizer.decode(s)
        return(output.split("### Response:")[1].strip())