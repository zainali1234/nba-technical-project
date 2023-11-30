export function updateDOM(games) {
  const modal = document.getElementById("myModal");
  const closeButton = document.querySelector(".close-button");
  const arrayContainer = document.getElementById("games-table");
  const shotsTable = document.getElementById("shots-table");

  closeButton.addEventListener("click", () => {
    modal.style.display = "none";
  });

  function removeAllRowsFromTable(table) {
    while (table.firstChild) {
      table.removeChild(table.firstChild);
    }
  }

  function createShotTableRow(shot) {
    const modalElement = document.createElement("tr");

    const makeValue = document.createElement("th");
    makeValue.textContent = shot.isMake ? "Yes" : "No";
    modalElement.appendChild(makeValue);

    const xCoord = Number(shot.locationX);
    const yCoord = Number(shot.locationY);
    const shotDistance = Math.sqrt(xCoord ** 2 + yCoord ** 2);

    const distValue = document.createElement("th");
    distValue.textContent = shotDistance.toFixed(2) + " ft";
    modalElement.appendChild(distValue);

    const pointValue = document.createElement("th");
    pointValue.textContent = shotDistance > 23.75 || Math.abs(xCoord) > 22.0 ? "3 pts" : "2 pts";
    modalElement.appendChild(pointValue);

    return modalElement;
  }

  function showGameDetails(game) {
    removeAllRowsFromTable(shotsTable);

    for (const shot of game.shots) {
      const modalElement = createShotTableRow(shot);
      shotsTable.appendChild(modalElement);
    }

    modal.style.display = "block";
  }

  for (const game of games) {
    const arrayElement = document.createElement("tr");
    const fields = [
      "date", "isStarter", "minutes", "points", "assists",
      "offensiveRebounds", "defensiveRebounds", "steals", "blocks",
      "turnovers", "defensiveFouls", "offensiveFouls",
      "freeThrowsMade", "freeThrowsAttempted", "twoPointersMade",
      "twoPointersAttempted", "threePointersMade", "threePointersAttempted"
    ];

    for (const field of fields) {
      const value = document.createElement("th");
      value.textContent = field === "isStarter" ? (game[field] ? "Yes" : "No") : game[field];
      arrayElement.appendChild(value);
    }

    arrayElement.addEventListener("click", () => {
      showGameDetails(game);
    });

    arrayElement.classList.add('clicked-row');
    arrayContainer.appendChild(arrayElement);
  }
}
