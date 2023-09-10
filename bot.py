import discord
r, mod = 283, 2147483647;
T = open("token.txt", 'r').read();
keyword = open("keyword.txt", 'r').read().split();
KW = [];
ints = discord.Intents.all();
bot = discord.Client(intents = ints);
def cut(S : str):
	T = "";
	for s in S:
		if ord(s) < 128 and (ord(s) < ord('a') or ord(s) > ord('z')):
			continue;
		else:
			T += s;
	return T;
def has(S : str):
	E = [];
	h, j, k, x = 0, 0, 0, 1;
	for i in range(len(S)):
		if S[i] >= 'a' and S[i] <= 'z':
			E.append(j);
			j += 1;
		else:
			j += 3;
	j = 0;
	S = S.encode("utf-8");
	for i in range(len(S)):
		if k < len(E) and i == E[k]:
			h = (h + (S[i] + 256) * x) % mod;
			k += 1;
		else:
			h = (h + S[i] * x) % mod;
		x = x * r % mod;
		j += 1;
	return [h, j];
def hsh(S : str):
	E, H = [], [0];
	j, k, x = 0, 0, 1;
	for i in range(len(S)):
		if S[i] >= 'a' and S[i] <= 'z':
			E.append(j);
			j += 1;
		else:
			j += 3;
	j = 0;
	S = S.encode("utf-8");
	for i in range(len(S)):
		if k < len(E) and i == E[k]:
			H.append((H[i] + (S[i] + 256) * x) % mod);
			k += 1;
		else:
			H.append(((H[i] + S[i] * x)) % mod);
		x = x * r % mod;
	return H;
def yellow(msg : str):
	S = hsh(msg);
	for [k, w] in KW:
		for i in range(1, len(S) - w + 1):
			if k == (S[i + w - 1] - S[i - 1] + mod) % mod:
				return 1;
			k = k * r % mod;
	return 0;
@bot.event
async def on_ready():
	for kw in keyword:
		KW.append(has(kw));
	print("logged in as", end = ' ');
	print(bot.user);
@bot.event
async def on_message(msg : discord.Message):
	if msg.author == bot.user:
		return;
	M = msg.content;
	M = cut(M.lower());
	if yellow(M):
		print("業績 + 1");
		await msg.channel.send(file = discord.File("swipe.png"));
		await msg.channel.send(file = discord.File("yellow.png"));
if __name__ == "__main__":
	bot.run(T);
