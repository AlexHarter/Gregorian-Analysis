#download all the vatican edition chants, separated by genre, then by mode
#Should I modify the default downloaded file name?  Include the modes in the file name, or just stick to the header within the files?

#from urllib.request import urlopen
from urllib import request
import re

usages = ("Introit", "Gradual", "Alleluia", "Tract", "Offertory", "Communion", "Antiphon", "Hymn", "Responsory")
usage_base_url = "https://gregobase.selapa.net/usage.php?id="
usage_ids = ("in", "gr", "al", "tr", "of", "co", "an", "hy", "re")

for usage_id in usage_ids:
	# Open page by usage
	usage_url = usage_base_url + usage_id
	usage_page = urlopen(usage_url)
	full_html = usage_page.read().decode("utf-8")
	#print(full_html)

	# Trim html string to just the content
	#print(re.split("<div id=\"content\">", full_html))
	content = re.split("<div id=\"content\">", full_html)[1]

	# Split the content string by entry
	entries = re.split("::marker\n<ahref=\"chant.php?id=", content)

	# Create list of only Vatican Edition entries
	vatican_chant_ids = []
	for entry in entries:
		if re.search("(Vatican)", entry).group() == "(Vatican)":
			vatican_chant_ids.append(re.search("\d{4,5}", entry).group())

	# Open webpage using chant id
	for chant_id in vatican_chant_ids:
		# TODO add proper folder
		chant_url = f"https://gregobase.selapa.net/download.php?id={chant_id}&format=gabc"
		response = request.urlretrieve(chant_url)
