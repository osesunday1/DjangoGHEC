var data1 = "{{data1}}"
        var data2 = "{{data2}}"
        var data3 = "{{data3}}"
        var data4 = "{{data4}}"

        var name1 = "{{name1}}"
        var name2 = "{{name2}}"
        var name3 = "{{name3}}"
        var name4 = "{{name4}}"


                const chartData = {
            labels: [name1, name2, name3, name4],
            data: [data1, data2, data3, data4],
          };
          
          const myChart = document.querySelector(".my-chart");
          const ul = document.querySelector(".programming-stats .details ul");
          
          new Chart(myChart, {
            type: "doughnut",
            data: {
              labels: chartData.labels,
              datasets: [
                {
                  label: "Language Popularity",
                  data: chartData.data,
                },
              ],
            },
            options: {
              borderWidth: 10,
              borderRadius: 2,
              hoverBorderWidth: 0,
              plugins: {
                legend: {
                  display: false,
                },
              },
            },
          });
          
          const populateUl = () => {
            chartData.labels.forEach((l, i) => {
              let li = document.createElement("li");
              li.innerHTML = `${l}: <span class='percentage'>${chartData.data[i]}%</span>`;
              ul.appendChild(li);
            });
          };
          
          populateUl();