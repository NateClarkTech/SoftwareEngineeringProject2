import { html, render, useState, useRef, useEffect, signal } from 'https://cdn.jsdelivr.net/npm/preact-htm-signals-standalone@0.0.16/+esm'

// Create the base URl for api calls
const currentPort = window.location.port;
const baseURL = `http://localhost:${currentPort}`

// A helper function to get JSON data from RestAPi endpoints
export const getJSON = async (url, content) => {
    try {
        // fetch data from the api 
        const response = await fetch(url, content)
        // convert to json
        const json = await response.json()
        // if its successful return failed(false) and the data
        return [false, json]
    } catch (e) {
        // incase of error, return failed(true) and no data
        console.log('fetch error', e)
        return [true, []]
    }
}

const App = () => {
    // state to store username 
    const [userName, setUserName] = useState('Guest');
    // state to store got messages
    const [messages, setMessages] = useState([])

    // Runs at mount, it sets websocket to listen to database signals to update
    useEffect(() => {
        // create a websocket
        const ws = new WebSocket(`ws://${location.host}/ws/chat/default/`)
        // listen for new messages
        ws.onmessage = (e) => {
            // fetch new messages from the server
            console.log('Update signal')
            loadMessages()
        }
        // load current messages from server 
        loadMessages()

    }, [])

    /**
     * Fetches all messages from the restapi
     */
    const loadMessages = async () => {
        // try fetch the data
        const [failed, response] = await getJSON(
            `${baseURL}/api/get_messages/`
        )
        // if succesful update the messages
        if (!failed) {
            const mes = response.mes
            setMessages(mes)
            scrollDown()
        } else {
            // if failed, log error message
            console.log(response, failed)
        }
    }
    /**
     * Adds a message to the database using the restapi 
     * @param {*} data the message contents
     */
    const addMessageToDB = async (data) => {
        const [failed, response] = await getJSON(
            `${baseURL}/api/add_message/`,
            {
                headers: {
                    "Content-Type": 'application/json',
                },
                method: 'post',
                body: JSON.stringify(data)
            }
        )
        if (!failed) {
            await loadMessages()
        } else {
            console.log(response, failed)
        }

    }
    /**
     * Removes a message with given id from the backend
     * @param {*} pos the index of the message
     */
    const deleteMessage = async (pos) => {
        // get message id
        const id = messages[pos].id
        // send delete request
        const [failed, response] = await getJSON(
            `${baseURL}/api/delete_message/${id}/`,
            {
                method: 'DELETE',
            }
        )
        // if delete succudes refresh messages
        if (!failed) {
            await loadMessages()
        } else {
            console.log(response, failed)
        }
    }
    // Get current time to set to new messages
    const getTime = (time) => {
        const date = new Date(time)
        return `${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getDate().toString().padStart(2, '0')}/${date.getFullYear()}`
    }
    // Scroll the chats page to the last message
    const scrollDown = () => {
        // select the end of messages marker
        const mesEnd = document.querySelector('#c-mes-end')
        // show new message, after a delay(wait for preact to update)
        setTimeout(() => {
            mesEnd.scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });
        }, 200);
    }

    // Function to create a new message to send
    const addmessage = () => {
        // Select message entry
        const mesInput = document.querySelector('#c-mes')
        // get typed message
        const mes = mesInput.value
        // check if message is of valid length
        if (mes.length < 2) {
            // if not valid length send alert to user
            alert('Enter message first')
            return
        }
        const user_name = window.user_name || "Guest";
        // create new message
        const newMes =
        {
            sender: user_name,
            val: mes,
            time: (new Date()).getTime(),
        }
        // post message to rest api
        addMessageToDB(newMes)
        // reset message field
        document.querySelector('#c-mes').value = ""
    }
    // check for enter key press
    const handleKeyPress = (event) => {
        // if enter key is pressed send message
        if (event.key === 'Enter') {
            addmessage()
        }
    };
    /**
     * A component that represent a row of message
     */
    const MessageRow = ({ mes, pos }) => {
        // state for whether delete is shown or not
        const [open, setOpen] = useState(false)

        // variable to hold popup
        let popup = null
        // if popup is open, set it to delete button
        if (open) {
            popup = html`
            <div class='c-opts' onClick=${() => deleteMessage(pos)} >
                <div>DELETE ? </div>
            </div>
            `
        }
        // render the message row
        return html`
            <div class='c-mes' >
                ${(window.user_name || "Guest") == mes.sender && html`<div  class='c-options' onClick=${() => setOpen(!open)} > ⚙️ </div>`}
                <div class='msg-content'>${mes.val}</div>
                <div class='c-mes-row' >
                    <div>${mes.sender}</div>
                    <div>${getTime(mes.time)}</div>
                </div>
                ${popup}
            </div>
        `
    }
    // render the chat page
    return html`
    <div class='c-body' >
        <div class="display-4 title-cont ">💬 NovoChat</div>
        
        <div class='c-messages' >
        ${messages.map((mes, pos) => {
        return html`
            <${MessageRow} mes=${mes} pos=${pos}  />
        `
    })}    
        <div id='c-mes-end' />
        </div>
        
        <div class='c-send-box' >
            <input placeholder='type message ... ' id='c-mes'
            onKeyPress=${handleKeyPress}  /> 
            <i class="fas fa-paper-plane"  onClick=${addmessage}  ></i>
        </div>     
    </div>
    `
}

// Mount the chat component into the chat page
render(
    html`<${App} />    `,
    document.getElementById('chats')
)