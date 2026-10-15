const input = document.getElementById("user-input");
const button = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");

// Send Button
button.addEventListener("click", sendMessage);

// Enter Key
input.addEventListener("keypress", function(event){

    if(event.key==="Enter"){

        sendMessage();

    }

});

function sendMessage(){

    let message=input.value.trim();

    if(message===""){

        return;

    }

    // User Message

    chatBox.innerHTML += `

        <div class="user-message">

            <strong>You</strong>

            <p>${message}</p>

        </div>

    `;

    input.value="";

    chatBox.scrollTop=chatBox.scrollHeight;

    // Flask Backend

    fetch("/chat",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            message:message

        })

    })

    .then(response=>response.json())

    .then(data=>{

        chatBox.innerHTML += `

        <div class="bot-message">

            <strong>Bot</strong>

            <p>${data.reply}</p>

        </div>

        `;

        chatBox.scrollTop=chatBox.scrollHeight;

    })

    .catch(error=>{

        chatBox.innerHTML += `

        <div class="bot-message">

            <strong>Bot</strong>

            <p>Server Error.</p>

        </div>`;
    });
}