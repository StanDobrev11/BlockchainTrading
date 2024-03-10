document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('tradingChart').getContext('2d');
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var chartData = {
        labels: months.slice(0, 12), // Initialize with the first 12 months
        datasets: [{
            label: 'Crypto Price',
            data: Array.from({length: 12}, () => Math.random() * 100 + 1000), // Starting data points
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1 // Adds smoothness to the line
        }]
    };

    var tradingChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            },
            animation: {
                duration: 300 // Slight animation for a smoother transition
            },
        }
    });

    // Function to generate a new data point close to the last one for smoother transition
    function generateNewDataPoint(lastValue) {
        return lastValue + (Math.random() - 0.5) * 20; // Smaller variance
    }

    // Update the chart at a set interval
    setInterval(() => {
        // Rotate month labels
        const nextMonth = months[(months.indexOf(chartData.labels[chartData.labels.length - 1]) + 1) % 12];
        chartData.labels.shift();
        chartData.labels.push(nextMonth);

        // Update data for a smoother transition
        chartData.datasets.forEach((dataset) => {
            const newDataPoint = generateNewDataPoint(dataset.data[dataset.data.length - 1]);
            dataset.data.shift();
            dataset.data.push(newDataPoint);
        });

        tradingChart.update();
    }, 1500); // Updating every second
});
