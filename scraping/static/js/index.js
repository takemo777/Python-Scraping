
$('#audio').on('click', () => {

    SpeechRecognition = webkitSpeechRecognition || SpeechRecognition; //chromeで音声認識
    const recognition = new SpeechRecognition();
    recognition.lang = 'ja-JP';


    recognition.onresult = (event) => {
         let result = event.results[0][0].transcript;
        result = result.slice(0, -1);
        $('#keyword').val(result);
    }

    recognition.start();
});
