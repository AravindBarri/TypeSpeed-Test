from time import time
import random
i = 0
cs = False
prompt = random.choice(["A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun. This disturbed the lion’s sleep, and he woke up quite angry. He was about to eat the mouse when the mouse desperately requested the lion to set him free. “I promise you, I will be of great help to you someday if you save me.” The lion laughed at the mouse’s confidence and let him go.",
"Birbal immediately smiled and went up to Akbar. He announced the answer; he said there were twenty-one thousand, five hundred and twenty-three crows in the city. When asked how he knew the answer, Birbal replied, “Ask your men to count the number of crows. If there are more, then the relatives of the crows must be visiting them from nearby cities. If there are fewer, then the crows from our city must be visiting their relatives who live outside the city.” Pleased with the answer, Akbar presented Birbal with a ruby and pearl chain.",
"The boy laughed at the fright he had caused. This time, the villagers left angrily. The third day, as the boy went up the small hill, he suddenly saw a wolf attacking his sheep. He cried as hard as he could, “Wolf! Wolf! Wolf!”, but not a single villager came to help him. The villagers thought that he was trying to fool them again and did not come to rescue him or his sheep. The little boy lost many sheep that day, all because of his foolishness.",
"One day, a selfish fox invited a stork for dinner. Stork was very happy with the invitation – she reached the fox’s home on time and knocked at the door with her long beak. The fox took her to the dinner table and served some soup in shallow bowls for both of them. As the bowl was too shallow for the stork, she couldn’t have soup at all. But, the fox licked up his soup quickly.",
"Once there lived a greedy man in a small town. He was very rich, and he loved gold and all things fancy. But he loved his daughter more than anything. One day, he chanced upon a fairy. The fairy’s hair was caught in a few tree branches. He helped her out, but as his greediness took over, he realised that he had an opportunity to become richer by asking for a wish in return (by helping her out). The fairy granted him a wish. He said, “All that I touch should turn to gold.” And his wish was granted by the grateful fairy."])

def counter():
	i = 0
	print("Upsolvers Labs - Student Community & Development Services\nOpen Software Access for learning")
	print("\n\n        Type the below paragraph as fast as you can and press enter only if completed           ")
	print("\n\n"+prompt+"\n\n")
	input(">> By pressing Enter will start measuring your typing speed and timer\n>> Press Enter to start \t\t")
	begin_time = time()
	inp = input("\n\n")
	end_time = time()
	final_time = (end_time - begin_time) / 60
	return final_time, inp


def wpm(time, line):
	words = line.split()
	word_length = len(words)
	words_per_m = word_length / time
	return words_per_m


def wordcheck(inp):
	prompts = prompt.split()
	inputs = inp.split()
	errorcount = 0
	
	idx = 0
	for inp in inputs:
		if inp != prompts[idx]:
			errorcount += 1
			if inp == prompts[idx + 1]:
				idx += 2
			elif inp != prompts[idx - 1]:
				idx += 1
		else:
			idx += 1

	words_left = len(prompts) - len(inputs)
	correct = float(len(prompts)) - float(errorcount)
	percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)

	
	return percentage


tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
print("You total time was: (0) minutes".format(tm))
print("with an average of: {0} words per minute".format(words_per_minute))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("with an accuracy of: {0} % accuracy".format(percentager))
