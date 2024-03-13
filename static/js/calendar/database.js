import { useEffect } from 'https://cdn.jsdelivr.net/npm/preact-htm-signals-standalone@0.0.16/+esm'
import { tasksSig } from "./store.js"

// const currentPort = window.location.port;
const currentPort = window.location.port;
const BASE_URL = `http://127.0.0.1:${currentPort}`


export const getUID = () => {
    return Math.floor(Math.random() * 100000)
}

export const addTask = (task) => {
    task = { ...task, id: getUID() }
    tasksSig.value = [task, ...tasksSig.value]
}

export const removeTask = (id) => {
    tasksSig.value = tasksSig.value.filter(t => t.id !== id)
}

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

export const getAllTasks = async () => {
    const id =  parseInt(window.user_id||0) 
    let [failed, res] = await getJSON(`${BASE_URL}/api/get_tasks/${id}/`)
    // console.log(failed, res)
    if (failed) {
        return []
    } else {
        console.log('task',id, res.tasks)
        return res.tasks
    }
}

export const addTaskToDB = async (data) => {
    let [failed, res] = await getJSON(`${BASE_URL}/api/add_task/`, {
        method: 'POST',
        body: JSON.stringify(data)
    })
    console.log(failed, res)
    if (!failed) {
        addTask({ ...data, id: res.data })
    }
    return !failed
}


export const deleteTaskFromDB = async (id) => {
    let [failed, res] = await getJSON(`${BASE_URL}/api/delete_task/${id}/`, {
        method: 'DELETE',
    })
    console.log(failed, res)
    if (!failed) {
        tasksSig.value = tasksSig.value.filter(t => t.id !== id)
    }
    return failed
}


export const addmessage = async (data) => {
    let [failed, res] = await getJSON(`${BASE_URL}/api/add_message`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    console.log(failed, res)
    if (failed) {
        return []
    } else {
        return res.tasks
    }
}

export const getAllMessage = async (data) => {
    let [failed, res] = await getJSON(`${BASE_URL}/api/get_messages`, data)
    console.log(failed, res)
    if (failed) {
        return []
    } else {
        return res.tasks
    }
}

export const useTasks = () => {
    useEffect(() => {
        (async () => {
            let allTasks = await getAllTasks()
            allTasks = [...allTasks, ...defaultTasks]
            tasksSig.value = allTasks
            console.log("Loaded tasks", tasksSig.value.length)
        })()
        console.log('called')
    }, [])

}


export const hamMessages = [
    "It's date for a delicious meal at HAM! Treat yourself.",
    "Feeling hungry? HAM is waiting for you! Enjoy your lunch.",
    "Don't forget to grab a bite at HAM. Your taste buds will thank you!",
    "Lunchtime alert! HAM has something special for you.",
    "Craving something tasty? Head to HAM and satisfy your appetite."
]

export const getHAMMessage = () => {
    const pos = Math.floor(Math.random() * hamMessages.length)
    return hamMessages[pos]
}

export const careMessages = [
    "Remember to take a deep breath and stretch. Your well-being matters!",
    "A short break can do wonders for your productivity. Take a moment for yourself.",
    "Don't forget to give your eyes a break. Look away from the screen and blink a few times.",
    "Taking breaks isn't a luxury; it's a necessity. Step away and recharge!",
    "Feeling stressed? A brisk walk can clear your mind and boost your energy.",
    "Your health is a priority. Take a break, go for a walk, and come back refreshed.",
    "Take a moment to enjoy some fresh air. A short walk can make a big difference.",
    "Sitting for too long? Stand up, stretch, and take a stroll around. Your body will thank you.",
    "Breaks aren't a sign of weakness; they're a sign of self-care. Treat yourself to a short pause.",
    "A change of scenery can do wonders. Step outside for a breath of fresh air.",
    "Listen to your body. If you need a break, take it. Your work will still be here when you return.",
    "Your mind functions better when it gets a chance to relax. Step away and rejuvenate.",
    "Taking breaks isn't slacking off; it's a smart strategy for long-term success.",
    "Feeling overwhelmed? A short walk can help clear your mind and reduce stress.",
    "A break may be the missing piece to solve that problem you've been pondering. Take a breather!",
]

export const getCareMessage = () => {
    const pos = Math.floor(Math.random() * careMessages.length)
    return careMessages[pos]
}


export const defaultTasks = [
    {
        "title": "January Interterm Begins",
        "date": "2024-01-03",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
        "time": [8, 30],
    },
    {
        "title": "January ISP Drop/Add Deadline",
        "date": "2024-01-05",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
        "time": [0, 0],
    },
    {
        "title": "Martin Luther King Jr. Day (No Classes; Offices Closed)",
        "date": "2024-01-15",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Baccalaureate Exam Report Due (for January Degree Conferral)",
        "date": "2024-01-19",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "New Student Move-In Day",
        "date": "2024-01-22",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Orientation for New Students",
        "date": "2024-01-24",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Mini-Classes",
        "date": "2024-01-25",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Mini-Classes",
        "date": "2024-01-26",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Report For-Credit Full-Term and Mod 1 Internships in Handshake Deadline",
        "date": "2024-01-26",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "January Interterm Ends",
        "date": "2024-01-26",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "January Degree Conferral",
        "date": "2024-01-26",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Spring Classes Begin",
        "date": "2024-01-29",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Spring Off-Campus Study (OCS) Contract and Tuition Waiver Deadline",
        "date": "2024-01-29",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Residency Reclassification Application Deadline",
        "date": "2024-02-02",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Contract Submission Deadline",
        "date": "2024-02-07",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Late Contract Submission Period ($50 Fee)",
        "date": "2024-02-08",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Late Contract Submission Period ($50 Fee)",
        "date": "2024-02-09",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Last Day for 100% Tuition Refund",
        "date": "2024-02-09",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Tuition and Fees Payment Deadline ($100 Penalty)",
        "date": "2024-02-09",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Presidents Day (No Classes; Offices Closed)",
        "date": "2024-02-19",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Last Day for 25% Tuition Refund",
        "date": "2024-02-23",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Financial Aid Unit Drop Grace Period Deadline",
        "date": "2024-02-23",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Report For-Credit Mod 2 Internships in Handshake Deadline",
        "date": "2024-03-15",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Final Payment Due on Payment Plans ($100 Penalty)",
        "date": "2024-03-15",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Module I Ends",
        "date": "2024-03-15",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Spring Break[STARTS]",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Spring Break[ENDS",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Module II Begins",
        "date": "2024-03-25",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Deadline to Request Readmission for Fall Semester",
        "date": "2024-04-01",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Thesis Prospectus Submission Deadline (6th Term)",
        "date": "2024-04-01",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Off-Campus Study (OCS) Declaration Deadline",
        "date": "2024-04-01",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Provisional AOC (PAOC) Submission Deadline (5th Term)",
        "date": "2024-04-01",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Fall Semester Registration Begins",
        "date": "2024-04-03",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Advising Day",
        "date": "2024-04-04",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Contract Renegotiation Deadline",
        "date": "2024-04-19",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Baccalaureate/Reading Days (No Classes)",
        "date": "2024-04-22",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Baccalaureate/Reading Days (No Classes)",
        "date": "2024-04-23",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Baccalaureate/Reading Days (No Classes)",
        "date": "2024-04-24",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Spring Classes End",
        "date": "2024-05-10",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Baccalaureate Examination Reports Due",
        "date": "2024-05-10",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Evaluation Submission Deadline (potential graduates)",
        "date": "2024-05-13",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Reading Days (No Classes)",
        "date": "2024-05-13",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Reading Days (No Classes)",
        "date": "2024-05-14",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Certification Submission Deadline (potential graduates)",
        "date": "2024-05-14",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Final Exams/Advising",
        "date": "2024-05-15",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Commencement (May, Aug, Jan degree conferrals included)",
        "date": "2024-05-17",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Evaluation Submission Deadline (students on probation)",
        "date": "2024-05-21",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Contract Certification Deadline (students on probation)",
        "date": "2024-05-22",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Memorial Day (Offices Closed)",
        "date": "2024-05-27",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Interterm ISP Evaluation Deadline",
        "date": "2024-05-29",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
    {
        "title": "Evaluation and Contract Submission Deadline",
        "date": "2024-05-29",
        "freq": "yearly",
        "type": "school",
        "hint": "no-save",
    },
].map(t => {
    const date = new Date(t.date)
    const time = t.time
    if (time) {
        date.setFullYear(date.getFullYear() - 1)
        date.setHours(time[0])
        date.setMinutes(time[1])
        console.log(time[0], time[1])
    } else {
        date.setHours(0)
        date.setMinutes(0)
    }
    return { ...t, time: date.getTime() }
})


