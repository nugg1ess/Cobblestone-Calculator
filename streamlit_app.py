import streamlit as st


def formatNumber(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return f"{number / 1000:.2f}K"
    elif number < 1000000000:
        return f"{number / 1000000:.2f}M"
    elif number < 1000000000000:
        return f"{number / 1000000000:.2f}B"
    elif number < 1000000000000000:
        return f"{number / 1000000000000:.2f}T"
    elif number < 1000000000000000000:
        return f"{number / 1000000000000000:.2f}QD"
    else:
        return f"{number / 1000000000000000000:.2f}QN"


def roman(number):
    if number == 1:
        return '<span style="color:#555555;">[<span style="color:#FFFFFF;">I<span style="color:#555555;">]'
    elif number == 2:
        return '<span style="color:#555555;">[<span style="color:#FFFFFF;">II<span style="color:#555555;">]'
    elif number == 3:
        return '<span style="color:#555555;">[<span style="color:#FFFFFF;">III<span style="color:#555555;">]'
    elif number == 4:
        return '<span style="color:#555555;">[<span style="color:#FFFFFF;">IV<span style="color:#555555;">]'
    elif number == 5:
        return '<span style="color:#555555;">[<span style="color:#FFFFFF;">V<span style="color:#555555;">]'

def getColor(str):
    if str == "wheat":
        return "#fcc200"
    elif str == "potato":
        return "#e7c16c"
    elif str == "carrot":
        return ""
    elif str == "beetroot":
        return "#fc4c49"


    elif str == "iron":
        return "#eabf7d"
    elif str == "amethyst":
        return "#bd00fc"

    elif str == "spruce":
        return "#007339"
    
    elif str == "cherry":
        return "#fc96fc"

    elif str == "auburn":
        return "#fc2424"
    elif str == "carmine":
        return "#9a0b0b"
    elif str == "cerulean":
        return "#2eaa7b"
    elif str == "azure":
        return "#004bfc"

    elif str == "rust":
        return "#b5400e"

    elif str == "superior":
        return "#ec1616"
    elif str == "inferior":
        return "#835737"
    
    elif str == "hageye":
        return "#c3fc19"

def createName(name, str, str1, num):
    loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,2,1,1])
    with loc3:
        return st.markdown(f"""
            <span style="
                background: linear-gradient(to right, {str}, {str1}, {str});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-weight: bold;
            ">{name}</span>
            <span style="color:#YOUR_COLOR; font-weight: bold;"> {roman(num)}</span>
            """, unsafe_allow_html=True)

def createBox(name, str, num):
    return st.markdown(f"""
        <div style="background-color: #gray; padding: 15px; border-radius: 5px; border: 2px solid {str};">
            <span style="color: #FFFFFF; font-weight: bold;">{name}:</span> 
            <span style="color: {str}; font-weight: bold;">{num}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
    <style>
            
    div.stButton > button[kind="secondary"] {
        background-color: #gray;
        color: white;
        border: 2px solid #555555;
    }
    div.stButton > button[kind="primary"] {
        background-color: #CB873B;
        color: white;
        border: 2px solid #EAAB65;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }
    
    .button-wrapper {
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

if 'selector' not in st.session_state:
    st.session_state.selector = "Toolmess"
if 'amount' not in st.session_state:
    st.session_state.amount = 1
if 'type' not in st.session_state:
    st.session_state.type = "All Materials"

loc1, titleLocation, loc2 = st.columns([1.9,8,1])
with titleLocation:
    st.title(
        body = ":orange[Cobblestone Calculator]",
        width = "stretch"
    )

st.divider()
loc1, loc2, loc3 = st.columns([1,1,1])
with loc2:
    st.markdown('<p style="white-space: nowrap;">Don\'t forget to select your material</p>', unsafe_allow_html=True)


loc1, toolmessButtonLocation, loc2, corrosiveButtonLocation, loc3 = st.columns([1,8,1,8,1])

with toolmessButtonLocation:
    if st.session_state.selector != "Toolmess":
        tt = "secondary"
    else:
        tt = "primary"
    if st.button(
        label = "Toolmess",
        use_container_width = True,
        type = tt
    ):
        st.session_state.selector = "Toolmess"
        st.rerun()

with corrosiveButtonLocation:
    if st.session_state.selector != "Corrosive":
        tt = "secondary"
    else:
        tt = "primary"
    if st.button(
        label = "Corrosive Essence",
        use_container_width = True,
        type = tt
    ):
        st.session_state.selector = "Corrosive"
        st.rerun()

st.divider()


loc1,loc2,loc3 = st.columns([1,1,1])
with loc2:
    st.markdown('<p style="white-space: nowrap; font-weight: bold;">How much are you making?</p>', unsafe_allow_html=True)
    num = st.text_input(
        label = "none",
        max_chars = 10,
        placeholder = "Enter Amount",
        label_visibility = "hidden",
        value = str(st.session_state.amount) if 'amount' in st.session_state else "1"

    #    icon = "😎"
    )


try:
    st.session_state.amount = int(num)
except ValueError:
    st.session_state.amount = 1
    st.error("Must choose to create 1 or more.")

st.divider()

select = []
if st.session_state.selector == "Toolmess":
    select = ["All Materials","Golden Hoe [V]","Iron Pickaxe [V]","Azure Extractor [V]","Twilight Scythe [V]"]
elif st.session_state.selector == "Corrosive":
    select = ["All Materials","Superior Mushroom Knife [V]","Enchanted Evoker [V]","The Soul Scythe [V]","Crystal Crusher [V]","Extras"]

loc1,loc2,loc3 = st.columns([1,1,1])
with loc2:
    st.markdown('<p style="white-space: nowrap; font-weight: bold;">What do you want to see?</p>', unsafe_allow_html=True)


option = st.selectbox(
    label = "",
    options = select,
)
st.session_state.type = option

st.divider()

type = st.session_state.type
selector = st.session_state.selector
num = st.session_state.amount


if selector == "Corrosive":

    if type == "Superior Mushroom Knife [V]":

        infTotal = formatNumber(622_500_000 * num)
        supTotal = formatNumber(307_500_000 * num)
        azureTotal = formatNumber(50_000_000 * num)
        auburnTotal = formatNumber(50_000_000 * num)

        inf1Azure = formatNumber(50_000_000 * num)
        inf1Auburn = formatNumber(50_000_000 * num)
        inf2Inf = formatNumber(25_500_000 * num)
        inf3Inf = formatNumber(60_000_000 * num)
        inf4Inf = formatNumber(105_000_000 * num)
        inf5Inf = formatNumber(105_000_000 * num)

        sup1Inf = formatNumber(180_000_000 * num)
        sup2Sup = formatNumber(37_500_000 * num)
        sup3Sup = formatNumber(75_000_000 * num)
        sup4Inf = formatNumber(45_000_000 * num)
        sup4Sup = formatNumber(120000000 * num)
        sup5Inf = formatNumber(105000000 * num)
        sup5Sup = formatNumber(75000000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Inferior Mushroom", getColor("inferior"), infTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Superior Mushroom", getColor("superior"), supTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        st.divider()
            

        createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 1)
        createBox("Auburn", getColor("auburn"), inf1Auburn)
        #st.markdown("<br>", unsafe_allow_html=True)
        createBox("Azure", getColor("azure"), inf1Azure)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 2)
        createBox("Inferior Mushroom", getColor("inferior"), inf2Inf)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 3)
        createBox("Inferior Mushroom", getColor("inferior"), inf3Inf)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 4)
        createBox("Inferior Mushroom", getColor("inferior"), inf4Inf)
        st.markdown("<br>", unsafe_allow_html=True)
          
        createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 5)
        createBox("Inferior Mushroom", getColor("inferior"), inf5Inf)
        st.markdown("<br>", unsafe_allow_html=True)
        st.divider()

        createName("Superior Mushroom Knife", getColor("inferior"),getColor("superior"), 1)
        createBox("Inferior Mushroom", getColor("inferior"), sup1Inf)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Superior Mushroom Knife", getColor("inferior"),getColor("superior"), 2)
        createBox("Superior Mushroom", getColor("superior"), sup2Sup)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Superior Mushroom Knife", getColor("inferior"),getColor("superior"), 3)
        createBox("Superior Mushroom", getColor("superior"), sup3Sup)
        st.markdown("<br>", unsafe_allow_html=True)
                    
        createName("Superior Mushroom Knife", getColor("inferior"),getColor("superior"), 4)
        createBox("Inferior Mushroom", getColor("inferior"), sup4Inf)
        createBox("Superior Mushroom", getColor("superior"), sup4Sup)
        st.markdown("<br>", unsafe_allow_html=True)
          
        createName("Superior Mushroom Knife", getColor("inferior"),getColor("superior"), 5)
        createBox("Inferior Mushroom", getColor("inferior"), sup5Inf)
        createBox("Superior Mushroom", getColor("superior"), sup5Sup)
        st.markdown("<br>", unsafe_allow_html=True)
        st.divider()

    elif type == "Enchanted Evoker [V]":
        wheatTotal = formatNumber(22500000 * num)
        potatoTotal = formatNumber(22500000 * num)
        beetrootTotal = formatNumber(22500000 * num)
        amethystTotal = formatNumber(180000000 * num)
        spruceTotal = formatNumber(31500000 * num)
        cherryTotal = formatNumber(252000000 * num)
        auburnTotal = formatNumber(486000000 * num)
        carmineTotal = formatNumber(513000000 * num)
        ceruleanTotal = formatNumber(564750000 * num)
        azureTotal = formatNumber(850500000 * num)

        auburn1Cherry = formatNumber(15_000_000 * num)
        auburn2Auburn = formatNumber(4500000 * num)
        auburn3Auburn = formatNumber(9000000 * num)
        auburn4Auburn = formatNumber(19500000 * num)
        auburn5Cherry = formatNumber(9000000 * num)
        auburn5Auburn = formatNumber(15000000 * num)

        carmine1Spruce = formatNumber(10500000 * num)
        carmine1Auburn = formatNumber(21000000 * num)
        carmine2Carmine = formatNumber(7500000 * num)
        carmine3Carmine = formatNumber(10500000 * num)
        carmine4Carmine = formatNumber(21000000 * num)
        carmine4Auburn = formatNumber(10500000 * num)
        carmine5Carmine = formatNumber(15000000 * num)

        cerulean1Wheat = formatNumber(7500000 * num)
        cerulean1Potato = formatNumber(7500000 * num)
        cerulean1Beetroot = formatNumber(7500000 * num)
        cerulean1Carmine = formatNumber(21000000 * num)
        cerulean2Cerulean = formatNumber(9000000 * num)
        cerulean3Cerulean = formatNumber(12750000 * num)
        cerulean4Carmine = formatNumber(13500000 * num)
        cerulean4Cerulean = formatNumber(15000000 * num)
        cerulean5Cerulean = formatNumber(25500000 * num)

        azure1Cerulean = formatNumber(36000000 * num)
        azure2Cerulean = formatNumber(7500000 * num)
        azure2Azure = formatNumber(7500000 * num)
        azure3Azure = formatNumber(21000000 * num)
        azure4Azure = formatNumber(30000000 * num)
        azure5Auburn = formatNumber(15000000 * num)
        azure5Carmine = formatNumber(15000000 * num)
        azure5Cerulean = formatNumber(15000000 * num)
        azure5Azure = formatNumber(15000000 * num)

        evoker1Azure = formatNumber(82500000 * num)
        evoker2Auburn = formatNumber(15000000 * num)
        evoker2Carmine = formatNumber(15000000 * num)
        evoker2Cerulean = formatNumber(15000000 * num)
        evoker2Azure = formatNumber(15000000 * num)
        evoker3Auburn = formatNumber(22500000 * num)
        evoker3Carmine = formatNumber(22500000 * num)
        evoker3Cerulean = formatNumber(22500000 * num)
        evoker3Azure = formatNumber(22500000 * num)
        evoker2Azure = formatNumber(15000000 * num)
        evoker4Auburn = formatNumber(30000000 * num)
        evoker4Carmine = formatNumber(30000000 * num)
        evoker4Cerulean = formatNumber(30000000 * num)
        evoker4Azure = formatNumber(30000000 * num)
        evoker5Amethyst = formatNumber(60000000 * num)
        evoker5Cherry = formatNumber(60000000 * num)
        evoker5Azure = formatNumber(60000000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Wheat", getColor("wheat"), wheatTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Potato", getColor("potato"), potatoTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Beetroot", getColor("beetroot"), beetrootTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Amethyst", getColor("amethyst"), amethystTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Spruce", getColor("spruce"), spruceTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Cherry", getColor("cherry"), cherryTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Auburn", getColor("auburn"), auburnTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Carmine", getColor("carmine"), carmineTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Cerulean", getColor("cerulean"), ceruleanTotal)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Azure", getColor("azure"), azureTotal)

        st.divider()
            

    elif type == "Extras":
        
        iron = formatNumber(10_000_000_000 * num)
        rust = formatNumber(10_000_000_000 * num)
        hageye = formatNumber(128 * num)

        createBox("Iron", getColor("iron"), iron)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Rust", getColor("rust"), rust)
        st.markdown("<br>", unsafe_allow_html=True)
        createBox("Hag Eye", getColor("hageye"), hageye)
        st.divider()


elif selector == "Toolmess":
    if type == "Extras":
        st.write("123")