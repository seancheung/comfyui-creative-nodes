import { app } from "../../scripts/app.js";

app.registerExtension({
  name: "creative.propagate",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    const isStop = nodeData.name === "CreativeStopFlow";
    const isSkipFrom = nodeData.name === "CreativeSkipFromFlow";
    const isSkipTo = nodeData.name === "CreativeSkipToFlow";
    if (isStop || isSkipFrom || isSkipTo) {
      nodeData.output = isSkipFrom ? ["*", "SKIP_FROM"] : ["*"];
      nodeData.output_is_list = isSkipFrom ? [false, false] : [false];
      nodeData.output_name = isSkipFrom ? ["output", "skip_from"] : ["output"];
      nodeType.prototype.onConnectionsChange = function (
        type,
        index,
        connected,
        link_info
      ) {
        if (!link_info) return;
        if (type == 2) {
          // connect output
          if (connected) {
            if (app.graph._nodes_by_id[link_info.target_id].type == "Reroute") {
              app.graph._nodes_by_id[link_info.target_id].disconnectInput(
                link_info.target_slot
              );
            }
            if (this.outputs[0].type == "*") {
              if (link_info.type == "*") {
                app.graph._nodes_by_id[link_info.target_id].disconnectInput(
                  link_info.target_slot
                );
              } else {
                // propagate type
                this.outputs[0].type = link_info.type;
                this.outputs[0].name = link_info.type;
                for (let i in this.inputs) {
                  if (this.inputs[i].name == "input")
                    this.inputs[i].type = link_info.type;
                }
              }
            }
          }
        } else {
          if (app.graph._nodes_by_id[link_info.origin_id].type == "Reroute")
            this.disconnectInput(link_info.target_slot);
          // connect input
          if (this.inputs[0].type == "*") {
            const node = app.graph.getNodeById(link_info.origin_id);
            let origin_type = node.outputs[link_info.origin_slot].type;

            if (origin_type == "*") {
              this.disconnectInput(link_info.target_slot);
              return;
            }

            if (origin_type == "SKIP_FROM") {
              return;
            }

            for (let i in this.inputs) {
              if (this.inputs[i].name == "input")
                this.inputs[i].type = origin_type;
            }

            this.outputs[0].type = origin_type;
            this.outputs[0].name = origin_type;
          }
        }
      };
    }
  },
});
