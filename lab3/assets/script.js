const launchDate = new Date('October 8, 2023 11:00:00').getTime()


const calculateDifference = () => {
    const now = new Date().getTime()
    return now - launchDate
}

const updateCounter = () => {
    const timeDifference = calculateDifference(launchDate)

    // Calculate the time in days, hours, minutes, seconds
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24))
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60))
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000)

    // Find the element we want to interact with by it's ID attribute
    const outputElement = document.getElementById('launch_counter')

    // Update the HTML of that element
    outputElement.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s "
}
