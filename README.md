
<!-- link I used to write the README: https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/ -->

<h1>Morse Code Webpage Translator</h1>

<h3>About the Project</h3>
<menu>
    <li><em>What is it?</em> A command-line Python application that translates 
    a given URL's HTML webpage data to Morse code.</li>
    <li><em>What does it do?</em> The app reads in a URL/hyperlink, fetches 
    the text from each tag in the URL's webpage using BeautifulSoup, 
    translates that text to Morse code, and prints each tag's Morse code
    info to the screen.</li>
    <li><em>What technologies does it use?</em> Pretty much just basic Python, 
    the Python <em>requests</em> library for handling HTML webpage data, and the
    Python <em>BeautifulSoup</em> library for web scraping.</li>
    <li><em>Why those technologies?</em> I have a strong foundation in Python,
    I think Morse Code is intriguing, and I find web scraping cool. Thus, I
    made a project combining all three concepts.</li>
    <li>
        <em>Some Challenges Faced</em>
        <ol>
            <li><em>Raspberry Pi</em>: my original idea was to translate a 
            sentence to Morse code, send the Morse data to a Raspberry Pi, and
            write code to make LEDs on the Pi blink the Morse code. 
            <br>
            <b>Problem:</b>
            I had never used a Raspberry Pi before. 
            <br>
            <b>Solution:</b> I researched intermediate Python projects instead,
            and found out about web scraping, then decided to try that.
            </li>
            <li><em>Fetching Webpage Data</em>: my new idea was to get webpage
            data with BeautifulSoup and translate that data to Morse code.
            <br>
            <b>Problem:</b>
            I struggled to fetch the data without messy tags getting in the way.
            I also wasn't sure which tags' info to fetch, since website tags are
            unpredictable compared to tags from static HTML pages.
            <br>
            <b>Solution:</b> I researched how to fetch all tags and their text 
            from a webpage with BeautifulSoup, and then went ahead to 
            implement that.
            </li>
        </ol>
    </li>
    <li>
        <em>Some Features to Implement in the Future</em>
        <ul>
            <li><em>Morse code translation for ALL tags</em> - 
            I filtered some 'meta' ones out for now.</li>
            <li>Raspberry Pi LED Morse Code - sending Morse-translated
            webpage data to a Raspberry Pi to be displayed with LEDs.</li>
        </ul>
    </li>
</menu>

<h3>Installing/Running the Project</h3>
<ol>
    <li>Make sure you have Python 3 installed.</li>
    <li>
        Install the <i>requests</i> and <i>BeautifulSoup</i> libraries.
    </li>
    <li>Clone this project.</li>
    <li>Using the URL from Step 3, clone this project to your 
    machine.</li>
    <li>Head over to the project directory; make sure the <i>main.py</i> file 
    is in that same directory.</li>
    <li>In the terminal, type <i>python main.py</i> for Windows. For MacOS or
    Linux or any similar UNIX-based OS, type <i>python3 main.py</i>.</li>
    <li>Enter your favorite website's URL when prompted.</li>
    <li>Congrats! Your URL's important content has been translated to 
    Morse code!</li>
</ol>

<h3>How to Use the Project</h3>
<menu>
    <li>
    Online communication has mostly phased out Morse code, but Wi-Fi and cell
service are still fragile and tentative. A few too many miles away from 
civilization often means no cell service.
    </li>
    <li>
    However, as long as one is able to make some kind of signal, Morse code 
    can be used without Wi-Fi, cell service, or any other requirement for 
    long-distance communication.
    </li>
    <li>Anyone can use this webpage translator to send useful content to
    friends even without cell service or Wi-Fi!</li>
</menu>