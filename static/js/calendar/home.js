import { html, render, useState, useRef, useEffect } from 'https://cdn.jsdelivr.net/npm/preact-htm-signals-standalone@0.0.16/+esm'

import { WeekCalender } from './WeekCalender.js'
import { DayCalender } from './DayCalender.js'
import { MonthCalender } from './MonthCalender.js'
import { SemCalender } from './YearCalender.js'
import { dateSig, monthSig, selectedDate } from './store.js'
import { yearSig } from './store.js'
import { getMonthName } from './days.js'
import CreatePopup from './CreatePopup.js'
import { useTasks } from './database.js'
import { MessagePopup } from './MessagePopup.js'

/**
 * This is the scheduler page
 */
const Home = () => {
    // The type of VIEW to show, set versions of state update it and redraws the UI
    const [viewType, setViewType] = useState('MONTH')
    const [createPopupOpen, setCreatePopupOpen] = useState(false)
    const dateTitleRef = useRef()
    const [width, setWidth] = useState()
    const isMobile = width < 500
    // check size and hide nav bar
    useEffect(() => {
        const resizeObserver = new ResizeObserver((entries) => {
            for (const entry of entries) {
                setWidth(entry.contentRect.width)
                const { target, contentRect } = entry;
                console.log(`Size of document body changed to ${contentRect.width}x${contentRect.height}`);
            }
        });
        resizeObserver.observe(document.body);
    }, [])

    // This is a custome hook, it managed the tasks, like loads and saves them has when they chnage or app loads
    useTasks()

   
    // THis hook, runs once when app loads and sets date to current date
    useEffect(() => {
        const now = (new Date())
        monthSig.value = now.getMonth()
        dateSig.value = now.getDate()
        yearSig.value = now.getFullYear()
    }, [])

    // This hook runs when yearSig or monthSig chnages and chnages the title of the date on the calender
    useEffect(() => {
        dateTitleRef.current.innerText = `${getMonthName(monthSig.value)} ${yearSig.value}`
    }, [yearSig.value, monthSig.value])

    // Closes the create task popup
    function closePopup() {
        setCreatePopupOpen(false)
    }

    // Opens the create task popup
    function openPopup() {
        setCreatePopupOpen(true)
    }

    // Next month clicked
    function nextClicked() {
        monthSig.value++
        if (monthSig.value > 11) {
            monthSig.value = 0
            yearSig.value++
        }
    }

    // prev month clicked
    function prevClicked() {
        monthSig.value--
        if (monthSig.value < 0) {
            monthSig.value = 11
            yearSig.value--
        }
    }

    // This is component, and draw one of the buttons for changing the VIew Type(DAY, WEEK ,etc)
    const ViewButton = ({ view }) => {

        // When the button is clicked, chnage view to its type
        const clicked = () => {
            setViewType(view)
        }
        // add more classes if this is the current view
        const extraClasses = view === viewType ? 'bg-primary' : ''
        // draw the actual view button
        return html`
            <button type="button" class=${`btn btn-outline-primary view-button ${extraClasses} `}
            onClick=${clicked}
            >
                ${view.toUpperCase()}
            </button>
        `
    }

    // this draws the scheduler page
    const mainStyles = isMobile ? 'max-width: 96.5vw' : 'max-width: 73.5vw';
    console.log(mainStyles)
    return html`
      <div class="body-cont">
        <!--MAIN SECTION-->
        <div class="main " style="${mainStyles}" >
            <div class="buttons">
                <${ViewButton} view="DAY"  />
                <${ViewButton} view="WEEK"  />
                <${ViewButton} view="MONTH"  />
                <${ViewButton} view="SEM"  />
            </div>
            <div class='create-title' >
                <div class="create-button " onClick=${openPopup} > 📝 new </div>
                <div class="date-row text-primary ">
                    <div  onClick=${prevClicked} >⬅️</div>
                    <h2 class="" ref=${dateTitleRef} >February 2024</h2>
                    <div  onClick=${nextClicked} >➡️</div>
                </div>
            </div>
            <!--This is a cnditional render, and draw only the current view -->
            <div class='calender-view' >
                ${viewType === 'WEEK' && html`
                    <${WeekCalender}   />
                `}
                ${viewType === 'DAY' && html`
                    <${DayCalender}   />
                `}
                ${viewType === 'MONTH' && html`
                    <${MonthCalender}   />
                `}
                ${viewType === 'SEM' && html`
                    <${SemCalender}   />
                `}
            </div>
        </div>

        <!-- WILL SHOW CREATE POPUP -->
        <${CreatePopup} open=${createPopupOpen} closePopup=${closePopup} />
        <${MessagePopup}  />

    </div>
    `

}

document.addEventListener('DOMContentLoaded', () => {
    console.log('loaded')
    const divElement = document.getElementById('calendar')
    console.log(divElement)
    render(html`<${Home} /> `, divElement)
})
