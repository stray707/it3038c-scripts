const express = require('express');
const app = express();
const os = require('os')
const PORT = 3000;

app.get('/', (req, res) => {

    const HOSTNAME = os.hostname();
    let IPADDR = "ERROR: NOT FOUND";
    let UPTIME = os.uptime();
    let TMEMORY = os.totalmem();
    let FMEMORY = os.freemem();
    let CORES = os.cpus().length;

    // Loop for finding IP of machine on the local network
    const interfaces = os.networkInterfaces();
    for (let interfaceName in interfaces ) {
        const addresses = interfaces [interfaceName];

        for (let addressInfo of addresses) {
            if (addressInfo.family === 'IPv4' && !addressInfo.internal) { 
                // checks for IPv4 and not loopback address
                IPADDR = addressInfo.address;
                break;
            }
        }
        if (IPADDR) {
            break;
        }
    }

    // Converting os.uptime() to time format string
    let days = 0;
    let hours = 0;
    let minutes = 0;
    let remainder = UPTIME

    days = Math.floor(UPTIME / 86400);
    remainder = UPTIME % 86400;

    hours = Math.floor(remainder / 3600);
    remainder = remainder % 3600;

    minutes = Math.floor(remainder / 60);
    seconds = remainder % 60;
    seconds = Math.round(seconds * 100) / 100;

    UPTIME = "Days: " + days + ", Hours: " + hours + ", Minutes: " + minutes + ", Seconds: " + seconds;

    // Converting total and free memory
    TMEMORY = Math.round(TMEMORY / (1024 * 1024)).toString() + " MB";
    FMEMORY = Math.round(FMEMORY / (1024 * 1024)).toString() + " MB";;



    res.send(`
        <html>
            <body>
                <p>Hostname: ${HOSTNAME}</p>
                <p>IP: ${IPADDR}</p>
                <p>Server Uptime: ${UPTIME}</p>
                <p>Total Memory: ${TMEMORY}</p>
                <p>Free Memory: ${FMEMORY}</p>
                <p>CPUs: ${CORES}</p>
            </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}/`);
});