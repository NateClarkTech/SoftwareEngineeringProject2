import { html, render, useState, useRef, useEffect, signal } from 'https://cdn.jsdelivr.net/npm/preact-htm-signals-standalone@0.0.16/+esm'

const currentPort = window.location.port;
const baseURL = `http://localhost:${currentPort}`


export const getJSON = async (url, content) => {
    try {
        const response = await fetch(url, content)
        const json = await response.json()
        return [false, json]
    } catch (e) {
        console.log('fetch error', e)
        return [true, []]
    }
}

let oldCont = -1
const App = () => {
    const [userName, setUserName] = useState('Guest');
    const [messages, setMessages] = useState([])


    useEffect(() => {
        const timer = setInterval(() => {
            loadMessages()
        }, 1000)
        loadMessages()
        setUserName(window.user_name || 'Guest')
        return () => clearInterval(timer)
    }, [])

    const loadMessages = async () => {
        const [failed, response] = await getJSON(
            `${baseURL}/api/get_messages/`
        )
        if (!failed) {
            const mes = response.mes
            if (mes.length != oldCont) {
                setMessages(mes)
                scrollDown()
                oldCont = mes.length
            }
        } else {
            console.log(response, failed)
        }
    }
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
    const deleteMessage = async (pos) => {

        const id = messages[pos].id
        const [failed, response] = await getJSON(
            `${baseURL}/api/delete_message/${id}/`,
            {
                method: 'DELETE',
            }
        )
        if (!failed) {
            await loadMessages()
        } else {
            console.log(response, failed)
        }

    }
    const getTime = (time) => {
        const date = new Date(time)
        return `${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getDate().toString().padStart(2, '0')}/${date.getFullYear()}`
    }
    const scrollDown = () => {
        const mesEnd = document.querySelector('#c-mes-end')
        // show new message, after a delay(wait for preact to update)
        setTimeout(() => {
            mesEnd.scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });
        }, 200);
    }
    const addmessage = () => {
        const mesInput = document.querySelector('#c-mes')
        const mes = mesInput.value
        if (mes.length < 2) {
            alert('Enter message first')
            return
        }
        const newMes =
        {
            sender: userName,
            val: mes,
            time: (new Date()).getTime(),
        }
        addMessageToDB(newMes)
        document.querySelector('#c-mes').value = ""
    }
    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            addmessage()
        }
    };

    const MessageRow = ({ mes, pos }) => {
        const [open, setOpen] = useState(false)

        let popup = null
        if (open) {
            popup = html`
            <div class='c-opts' onClick=${() => deleteMessage(pos)} >
                <div>DELETE ? </div>
            </div>
            `
        }
        return html`
            <div class='c-mes' >
                ${userName == mes.sender && html`<div  class='c-options' onClick=${() => setOpen(!open)} > ⚙️ </div>`}
                <div class='msg-content'>${mes.val}</div>
                <div class='c-mes-row' >
                    <div>${mes.sender}</div>
                    <div>${getTime(mes.time)}</div>
                </div>
                ${popup}
            </div>
        `
    }
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

render(
    html`<${App} />    `,
    document.getElementById('chats')
)