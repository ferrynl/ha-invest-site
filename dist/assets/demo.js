const series = {
  "1M": ["€ 24.860", "+2,1%", "M0 87 L32 80 62 85 93 62 128 65 163 41 195 45 229 29 260 37 300 15"],
  "1Y": ["€ 24.860", "+12,8%", "M0 105 L32 91 62 98 93 73 128 79 163 54 195 63 229 44 260 48 300 15"],
  "ALL": ["€ 24.860", "+24,3%", "M0 113 L32 111 62 97 93 105 128 83 163 68 195 78 229 52 260 58 300 15"]
};
const buttons = document.querySelectorAll("[data-period]");
for (const button of buttons) {
  button.addEventListener("click", () => {
    const [value, change, path] = series[button.dataset.period];
    document.querySelector("#value").textContent = value;
    document.querySelector("#change").textContent = change;
    document.querySelector(".chart path").setAttribute("d", path);
    for (const item of buttons) item.setAttribute("aria-pressed", String(item === button));
  });
}
