Project status
Development will basically end from my side until I need to webscrape more stuff later on.
If others want to do something with this, request to fork it, and build on to the project. If I feel the project is turning into something else then from the original intent, I'll request that you copy this project and start a whole new project, with the acknowledgment of using this as base code. That would be fine.
If I learn python updates have rendered this code useless, I'll might try to update it then.

Name
Amazon/website books webscraper

Description
This python program scrapes html files of Amazon book webpages that you want to collect various book details from.
This program is very effective at going through an entire folder of html files and scraping details,
then it can output it to the console.log() or .json file.

Usage
1. Navigate to specific Amazon webpage.
2. Right Click 'Save As'. Save this webpage as a html file.
3. Determine information you want to collect.
4. Open .html file and right click webpage element/information you want to collect. Click 'Inspect' (using Chrome browser).
5. This step, you should be familiar with HTML markup. You'll need to identify some unique 'id', 'class', or other tags (img, src, for example).
6. After identifying markups, you might have to adjust the code in the index.js file so that the program finds and extracts the information you want.
7. Run the python script. It should output to the console and to a json file. 
8. Inspect the output to be sure this is what you are looking for.

Support
Original script was created with GPT prompts. Modified for this specific case. Consult sources on the web if problems come up, or don't understand something with the script.

Roadmap
Probably further modification as more products are scraped. Automating going to specific product pages and "saving as html" process could happen. A roadblock is websites check if it's a bot accessing the webpage. Also, only a portion of the webpage initially loads, and more is loaded when you scroll down. Need to automate this as well. Maybe.

Contributing
Feel free to use this code as is, or copy/branch/fork it out to modify it how ever you see fit without tampering with the original codebase. I'm not responsible for your reprecussions if you use this code or anything similar to this code for whatever.

Authors and acknowledgment
Myself, N. Poduska, and ChatGPT. But mostly just myself, as GPT was like a drunk partner who produced stuff that looks like it should work, but it doesn't. Then a human has to fix it. And it was faster just to format the code myself. 

License
Open sauze. 

