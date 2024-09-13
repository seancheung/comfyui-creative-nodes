import server

def onprompt_for_flow(json_data):
    stop_flow_info = {}
    
    for k, v in json_data['prompt'].items():
        if 'class_type' not in v:
            continue
        cls = v['class_type']
        if cls == 'CreativeStopFlow':
            stop_flow_info[k] = v['inputs']['enabled']
            
    for k, v in json_data['prompt'].items():
        disable_targets = set()
        for kk, vv in v['inputs'].items():
            if isinstance(vv, list) and len(vv) == 2:
                if vv[0] in stop_flow_info:
                    if stop_flow_info[vv[0]]:
                        disable_targets.add(kk)
        for kk in disable_targets:
            del v['inputs'][kk]

def onprompt(json_data):
    try:
        onprompt_for_flow(json_data)
    except Exception as e:
        print(f"[WARN] Creative: Error on prompt - several features will not work.\n{e}")

    return json_data

server.PromptServer.instance.add_on_prompt_handler(onprompt)