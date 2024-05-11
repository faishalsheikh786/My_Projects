import { useState } from 'react';
import './CaseConverter.css'

function CaseConverter(){
    const [text, setText] = useState('')
    const [error, setError] = useState('')

    function handlechange(event){
        setText(event.target.value)
    }

    function changeUppercase(){
        setText(text.toUpperCase())
    }


    function changeLowercase(){
        setText(text.toLowerCase())
    }


    function sentencecase() {
        // Split the text into sentences using regular expression
        let sentences = text.split(/\. /);
    
        // Capitalize the first letter of each sentence
        for (let i = 0; i < sentences.length; i++) {
            sentences[i] = sentences[i].charAt(0).toUpperCase() + sentences[i].substring(1);
        }
        
        // Join the sentences back into a text
        setText(sentences.join('. '));
    }
    


    function capitalisecase(){
        let words = text.toLowerCase().split('. ');
        // Capitalize the first letter of each word
        for (let i = 0; i < words.length; i++) {
            words[i] = words[i].charAt(0).toUpperCase() + words[i].substring(1);
        }
        // Join the words back into a sentence
        setText(words.join('. '))
    }


    function titlecase(){
        let words = text;
        words = words.charAt(0).toUpperCase()+words.substring(1);
        setText(words)
    }


    function removeblankspace() {
        setText(text.replace(/\s+/g, ' ').trim());
    }

    function clear(){
        setText('')
    }


    function copytoclipboard(){
        // Check if text is empty
        if (text === '') {
            // If text is empty, copy an empty string to the clipboard
            navigator.clipboard.writeText('');
            return;
        }
    
        // Select the text area
        const textArea = document.createElement('textarea');
        textArea.value = text;
    
        // Append the text area to the DOM
        document.body.appendChild(textArea);
    
        // Select the text in the text area
        textArea.select();
    
        // Copy the selected text to clipboard
        document.execCommand('copy');
    
        // Remove the text area from the DOM
        document.body.removeChild(textArea);
    }

    function paste() {
        let clipboardText; // Variable to store the clipboard text
    
        navigator.clipboard.readText()
        .then(text => {
            clipboardText = text; // Store the clipboard text in the variable
            setText(clipboardText); // Update the textarea with the clipboard text
        })
    }



    function downloadtext(){
        function clearError() {
            setError('');
        }
        if (text!==''){
                // Create a Blob object from the text
                const blob = new Blob([text], { type: 'text/plain' });

                // Create a temporary anchor element
                const anchor = document.createElement('a');

                // Set the href attribute of the anchor to a URL created from the Blob
                anchor.href = window.URL.createObjectURL(blob);

                // Set the download attribute of the anchor
                anchor.download = 'text.txt';

                // Simulate a click on the anchor element to trigger the download
                anchor.click();

                // Clean up by revoking the URL created from the Blob
                window.URL.revokeObjectURL(anchor.href);
    }
    else{
        setError("Please enter some text first !")
        setTimeout(clearError, 2000);
    }
    }

    function wordcount(){
            // Remove leading and trailing whitespaces
            let newtext = text.trim();

            // Split the text into words using whitespace as delimiter
            const words = newtext.split(/\s+/);

            // Filter out empty strings from the array (caused by consecutive whitespaces)
            const filteredWords = words.filter(word => word !== '');

            // Return the length of the filtered array, which represents the number of words
            return filteredWords.length;
    }

    function charactercount(){
        return text.length
    }


    return(
        <div className="container">
            <h1>Text Coverter</h1>
            <div className="mb-6">
                <textarea className="form-control" id="exampleFormControlTextarea1" rows="6" value={text} onChange={handlechange} placeholder="Enter Text Here"></textarea>
            </div>
            <p className='error'>{error}</p>
            <div className='text-container'>
                <h2>Text Analysis</h2>
                <p className='details'><span>{wordcount()>=2?'Words':'Word'} : {wordcount()}</span><span className='remove'>  |  </span><span>{charactercount()>=2?'Characters':'Character'} : {charactercount()}</span></p>
            </div>

            <div className='buttons'>
            <button type="button" className="button" onClick={changeUppercase}>UpperCase</button>
            <button type="button" className="button"onClick={changeLowercase}>LowerCase</button>
            <button type="button" className="button"onClick={sentencecase}>SentenceCase</button>
            <button type="button" className="button"onClick={capitalisecase}>CapitaliseCase</button>
            <button type="button" className="button"onClick={titlecase}>TitleCase</button>
            <button type="button" className="button"onClick={removeblankspace}>RemoveBlankSpace</button>
            <button type="button" className="button"onClick={clear}>Clear</button>
            <button type="button" className="button"onClick={copytoclipboard}>Copy</button>
            <button type="button" className="button"onClick={paste}>Paste</button>
            <button type="button" className="button"onClick={downloadtext}>DownloadText</button>
            </div>

        </div>
    )
}

export default CaseConverter;