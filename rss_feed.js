document.addEventListener("DOMContentLoaded", function() {
    // Specify the RSS feed URL
    const rssFeedUrl = "https://www.sciencedaily.com/rss/top/science.xml";

    // Fetch the RSS feed
    fetch(rssFeedUrl)
        .then(response => response.text())
        .then(data => {
            // Parse the RSS feed XML data (you may need a library for more complex parsing)
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(data, "text/xml");

            // Extract and display feed items
            const items = xmlDoc.querySelectorAll("item");
            const feedContainer = document.getElementById("rss-feed");

            items.forEach(item => {
                const title = item.querySelector("title").textContent;
                const link = item.querySelector("link").textContent;
                const description = item.querySelector("description").textContent;

                const feedItem = document.createElement("div");
                feedItem.innerHTML = `<h2><a href="${link}" target="_blank">${title}</a></h2><p>${description}</p>`;
                feedContainer.appendChild(feedItem);
            });
        })
        .catch(error => {
            console.error("Error fetching RSS feed:", error);
        });
});
