import { app } from "../../scripts/app.js";

app.registerExtension({
  name: "creative.appearance",
  nodeCreated(node) {
    switch (node.comfyClass) {
      case "CreativeStopFlow":
      case "CreativeSkipFromFlow":
        {
          node.bgcolor = "#000000";
        }
        break;
    }
  },
});
