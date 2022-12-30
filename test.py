import trlx
trainer = trlx.train('gpt2', reward_fn=lambda samples: [sample.count('cats') for sample in samples])
