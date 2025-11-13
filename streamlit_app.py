import streamlit as st


st.set_page_config(
    page_title="Cobblestone Calculator",
    page_icon=":stuck_out_tongue:",
)

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
        return "#fc6e00"
    elif str == "beetroot":
        return "#fc4c49"

    elif str == "coal":
        return "#272a32"
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

    elif str == "twilight":
        return "#fcb500"
    elif str == "abyss":
        return "#0004fc"
    elif str == "ender":
        return "#da00fc"
    elif str == "void":
        return "#5a0000"

    elif str == "crystal":
        return "#5500b6"

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
        <div style="background-color: #gray; padding: 15px; border-radius: 18px; border: 1.5px solid {str};">
            <span style="color: #FFFFFF; font-weight: bold;">{name}:</span> 
            <span style="color: {str}; font-weight: bold;">{num}</span>
        </div>
        """, unsafe_allow_html=True)

#def createSelector(list): str:
#    st.selectbox(
#        label = "nothing",
#        label_visibility = "hidden",
#        options = list,
#    )

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
loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,3,1,1])
with loc3:
    st.markdown('<p style="white-space: nowrap;">Any issues? Contact me on discord; nugg1ess</p>', unsafe_allow_html=True)



st.divider()
loc1, loc2, loc3 = st.columns([1,1,1])
with loc2:
    st.markdown('<p style="white-space: nowrap; font-weight: bold;">What are you creating?</p>', unsafe_allow_html=True)


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
switcher = []
if st.session_state.selector == "Toolmess":
    select = ["All Materials","Golden Hoe [V]","Iron Pickaxe [V]","Azure Extractor [V]","Twilight Scythe [V]"]
    switcher = ["Golden Hoe [V]","Iron Pickaxe [V]","Azure Extractor [V]","Twilight Scythe [V]"]
elif st.session_state.selector == "Corrosive":
    select = ["All Materials","Superior Mushroom Knife [V]","Enchanted Evoker [V]","The Soul Scythe [V]","Crystal Crusher [V]","Extras"]
    switcher = ["Superior Mushroom Knife [V]","Enchanted Evoker [V]","The Soul Scythe [V]","Crystal Crusher [V]"]

loc1,loc2,loc3 = st.columns([1,1,1])
with loc2:
    st.markdown('<p style="white-space: nowrap; font-weight: bold;">What do you want to see?</p>', unsafe_allow_html=True)


option = st.selectbox(
    label = "nothing",
    label_visibility = "hidden",
    options = select,
)
st.session_state.type = option

st.divider()

type = st.session_state.type
selector = st.session_state.selector
num = st.session_state.amount


if selector == "Corrosive":
    if type == "All Materials":

        infTotal = formatNumber(622_500_000 * num)
        supTotal = formatNumber(307_500_000 * num)
        ironTotal = formatNumber(10000000000 * num)
        cherryTotal = formatNumber((10_000_000_000 * 3) * num)
        auburnTotal = formatNumber(((50_000_000)+(10_000_000_000 * 3)) * num)
        carmineTotal = formatNumber((10_000_000_000 * 3) * num)
        ceruleanTotal = formatNumber((10_000_000_000 * 3) * num)
        azureTotal = formatNumber(((50_000_000)+(10_000_000_000 * 3)+(20_000_000_000)) * num)
        twilightTotal = formatNumber(20000000000 * num)
        abyssTotal = formatNumber(20000000000 * num)
        enderTotal = formatNumber(20000000000 * num)
        voidTotal = formatNumber(20000000000 * num)

        rustTotal = formatNumber(10000000000 * num)

        crusherTotal = formatNumber(1 * num)
        crystalTotal = formatNumber(1_900_000_000 * num)

        hageyeTotal = formatNumber(64 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Inferior Mushroom", getColor("inferior"), infTotal)
        createBox("Superior Mushroom", getColor("superior"), supTotal)
        createBox("Iron", getColor("iron"), ironTotal)
        createBox("Cherry", getColor("cherry"), cherryTotal)
        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Carmine Fungus", getColor("carmine"), carmineTotal)
        createBox("Cerulean Fungus", getColor("cerulean"), ceruleanTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        createBox("Twilight Coral", getColor("twilight"), twilightTotal)
        createBox("Abyss Coral", getColor("abyss"), abyssTotal)
        createBox("Ender Coral", getColor("ender"), enderTotal)
        createBox("Void Coral", getColor("void"), voidTotal)
        createBox("End Crystal", getColor("crystal"), crystalTotal)
        createBox("Rust", getColor("rust"), rustTotal)

        st.markdown("<br>", unsafe_allow_html=True)     
        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Boss Drops</p>', unsafe_allow_html=True)
        
        createBox("Crystal Crusher [I]", getColor("crystal"), crusherTotal)
        createBox("Hag Eye", getColor("hageye"), hageyeTotal)


    elif type == "Superior Mushroom Knife [V]":

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

        createBox("Inferior Mushroom", getColor("inferior"), infTotal)
        createBox("Superior Mushroom", getColor("superior"), supTotal)
        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        st.divider()
            
        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Inferior Mushroom Knife","Superior Mushroom Knife"]
        )

        if switch == "Inferior Mushroom Knife":
            createName("Inferior Mushroom Knife", getColor("inferior"),getColor("inferior"), 1)
            createBox("Auburn", getColor("auburn"), inf1Auburn)
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
        elif switch == "Superior Mushroom Knife":
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


    elif type == "Enchanted Evoker [V]":

        cherryTotal = formatNumber(10000000000 * num * 3)
        auburnTotal = formatNumber(10000000000 * num * 3)
        carmineTotal = formatNumber(10000000000 * num * 3)
        ceruleanTotal = formatNumber(10000000000 * num * 3)
        azureTotal = formatNumber(10000000000 * num * 3)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,2,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount (3x for more tools)</p>', unsafe_allow_html=True)

        createBox("Cherry", getColor("cherry"), cherryTotal)
        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Carmine Fungus", getColor("carmine"), carmineTotal)
        createBox("Cerulean Fungus", getColor("cerulean"), ceruleanTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)



    elif type == "The Soul Scythe [V]":

        azureTotal = formatNumber(20000000000 * num)
        twilightTotal = formatNumber(20000000000 * num)
        abyssTotal = formatNumber(20000000000 * num)
        enderTotal = formatNumber(20000000000 * num)
        voidTotal = formatNumber(20000000000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,2,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Azure Roots", getColor("azure"), azureTotal)
        createBox("Twilight Coral", getColor("twilight"), twilightTotal)
        createBox("Abyss Coral", getColor("abyss"), abyssTotal)
        createBox("Ender Coral", getColor("ender"), enderTotal)
        createBox("Void Coral", getColor("void"), voidTotal)

    elif type == "Crystal Crusher [V]":

        crusherTotal = formatNumber(1 * num)
        crystalTotal = formatNumber(1900000000 * num)

        crystal1Crusher = formatNumber(1 * num)
        crystal2Crystal = formatNumber(50000000 * num)
        crystal3Crystal = formatNumber(250000000 * num)
        crystal4Crystal = formatNumber(350000000 * num)
        crystal5Crystal = formatNumber(1250000000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Crystal Crusher [I]", getColor("crystal"), crusherTotal)
        createBox("Crystal", getColor("crystal"), crystalTotal)
        st.divider()
            
        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Crystal Crusher"]
        )

        if switch == "Crystal Crusher":
            createName("Crystal Crusher", getColor("crystal"),getColor("crystal"), 1)
            createBox("Crystal Crusher [I]", getColor("crystal"), crystal1Crusher)
            st.markdown("<br>", unsafe_allow_html=True)       
            createName("Crystal Crusher", getColor("crystal"),getColor("crystal"), 2)
            createBox("End Crystal", getColor("crystal"), crystal2Crystal)
            st.markdown("<br>", unsafe_allow_html=True)     
            createName("Crystal Crusher", getColor("crystal"),getColor("crystal"), 3)
            createBox("End Crystal", getColor("crystal"), crystal3Crystal)
            st.markdown("<br>", unsafe_allow_html=True)        
            createName("Crystal Crusher", getColor("crystal"),getColor("crystal"), 4)
            createBox("End Crystal", getColor("crystal"), crystal4Crystal)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Crystal Crusher", getColor("crystal"),getColor("crystal"), 5)
            createBox("End Crystal", getColor("crystal"), crystal5Crystal)
            st.markdown("<br>", unsafe_allow_html=True)

    elif type == "Extras":
        
        iron = formatNumber(10000000000 * num)
        rust = formatNumber(10000000000 * num)
        hageye = formatNumber(64 * num)

        createBox("Iron", getColor("iron"), iron)
        createBox("Rust", getColor("rust"), rust)
        createBox("Hag Eye", getColor("hageye"), hageye)


elif selector == "Toolmess":
    if type == "All Materials":

        wheatTotal = formatNumber(7844414 * num)
        carrotTotal = formatNumber(198750 * num)
        potatoTotal = formatNumber(7799000 * num)
        beetrootTotal = formatNumber(8507500 * num)
        coalTotal = formatNumber(1550000 * num)
        ironTotal = formatNumber(700000 * num)
        spruceTotal = formatNumber(85500000 * num)
        cherryTotal = formatNumber(24000000 * num)
        auburnTotal = formatNumber(94500000 * num)
        carmineTotal = formatNumber(103500000 * num)
        ceruleanTotal = formatNumber(120750000 * num)
        azureTotal = formatNumber(273500000 * num)
        twilightTotal = formatNumber(312500000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Wheat", getColor("wheat"), wheatTotal)
        createBox("Carrot", getColor("carrot"), carrotTotal)
        createBox("Potato", getColor("potato"), potatoTotal)
        createBox("Beetroot", getColor("beetroot"), beetrootTotal)
        createBox("Coal", getColor("coal"), coalTotal)
        createBox("Iron", getColor("iron"), ironTotal)
        createBox("Spruce", getColor("spruce"), spruceTotal)
        createBox("Cherry", getColor("cherry"), cherryTotal)
        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Carmine Fungus", getColor("carmine"), carmineTotal)
        createBox("Cerulean Fungus", getColor("cerulean"), ceruleanTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        createBox("Twilight Coral", getColor("twilight"), twilightTotal)

    elif type == "Golden Hoe [V]":

        wheatTotal = formatNumber(344414 * num)
        carrotTotal = formatNumber(198750 * num)
        potatoTotal = formatNumber(299000 * num)
        beetrootTotal = formatNumber(307500 * num)

        wooden1Wheat = formatNumber(50 * num)
        wooden2Wheat = formatNumber(32 * num)
        wooden3Wheat = formatNumber(32 * num)
        wooden4Wheat = formatNumber(200 * num)
        wooden5Wheat = formatNumber(500 * num)

        stone1Wheat = formatNumber(100 * num)
        stone2Carrot = formatNumber(500 * num)
        stone3Carrot = formatNumber(1500 * num)
        stone4Carrot = formatNumber(2250 * num)
        stone5Wheat = formatNumber(3500 * num)
        stone5Carrot = formatNumber(3500 * num)

        iron1Carrot = formatNumber(8500 * num)
        iron2Potato = formatNumber(2000 * num)
        iron3Potato = formatNumber(3000 * num)
        iron4Potato = formatNumber(4000 * num)
        iron5Carrot = formatNumber(7500 * num)
        iron5Potato = formatNumber(5000 * num)

        diamond1Potato = formatNumber(15000 * num)
        diamond2Potato = formatNumber(5000 * num)
        diamond2Beetroot = formatNumber(5000 * num)
        diamond3Beetroot = formatNumber(12500 * num)
        diamond4Wheat = formatNumber(15000 * num)
        diamond4Potato = formatNumber(15000 * num)
        diamond4Beetroot = formatNumber(15000 * num)
        diamond5Potato = formatNumber(25000 * num)
        diamond5Beetroot = formatNumber(50000 * num)

        golden1Wheat = formatNumber(25000 * num)
        golden1Carrot = formatNumber(25000 * num)
        golden1Potato = formatNumber(25000 * num)
        golden1Beetroot = formatNumber(25000 * num)
        golden2Potato = formatNumber(50000 * num)
        golden2Beetroot = formatNumber(50000 * num)
        golden3Wheat = formatNumber(150000 * num)
        golden4Wheat = formatNumber(50000 * num)
        golden4Carrot = formatNumber(50000 * num)
        golden4Potato = formatNumber(50000 * num)
        golden4Beetroot = formatNumber(50000 * num)
        golden5Wheat = formatNumber(100000 * num)
        golden5Carrot = formatNumber(100000 * num)
        golden5Potato = formatNumber(100000 * num)
        golden5Beetroot = formatNumber(100000 * num)


        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Wheat", getColor("wheat"), wheatTotal)
        createBox("Carrot", getColor("carrot"), carrotTotal)
        createBox("Potato", getColor("potato"), potatoTotal)
        createBox("Beetroot", getColor("beetroot"), beetrootTotal)

        st.divider()

        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Wooden Hoe","Stone Hoe","Iron Hoe","Diamond Hoe","Golden Hoe"]
        )

        if switch == "Wooden Hoe":
            createName("Wooden Hoe", getColor("wheat"),getColor("wheat"), 1)
            createBox("Wheat", getColor("wheat"), wooden1Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Wooden Hoe", getColor("wheat"),getColor("wheat"), 2)
            createBox("Wheat", getColor("wheat"), wooden2Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Wooden Hoe", getColor("wheat"),getColor("wheat"), 3)
            createBox("Wheat", getColor("wheat"), wooden3Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Wooden Hoe", getColor("wheat"),getColor("wheat"), 4)
            createBox("Wheat", getColor("wheat"), wooden4Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Wooden Hoe", getColor("wheat"),getColor("wheat"), 5)
            createBox("Wheat", getColor("wheat"), wooden5Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
        elif switch == "Stone Hoe":
            createName("Stone Hoe", getColor("carrot"),getColor("carrot"), 1)
            createBox("Wheat", getColor("wheat"), stone1Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Stone Hoe", getColor("carrot"),getColor("carrot"), 2)
            createBox("Carrot", getColor("carrot"), stone2Carrot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Stone Hoe", getColor("carrot"),getColor("carrot"), 3)
            createBox("Carrot", getColor("carrot"), stone3Carrot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Stone Hoe", getColor("carrot"),getColor("carrot"), 4)
            createBox("Carrot", getColor("carrot"), stone4Carrot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Stone Hoe", getColor("carrot"),getColor("carrot"), 5)
            createBox("Wheat", getColor("wheat"), stone5Wheat)
            createBox("Carrot", getColor("carrot"), stone5Carrot)
            st.markdown("<br>", unsafe_allow_html=True)
        elif switch == "Iron Hoe":
            createName("Iron Hoe", getColor("potato"),getColor("potato"), 1)
            createBox("Carrot", getColor("carrot"), iron1Carrot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Hoe", getColor("potato"),getColor("potato"), 2)
            createBox("Potato", getColor("potato"), iron2Potato)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Hoe", getColor("potato"),getColor("potato"), 3)
            createBox("Potato", getColor("potato"), iron3Potato)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Hoe", getColor("potato"),getColor("potato"), 4)
            createBox("Potato", getColor("potato"), iron4Potato)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Hoe", getColor("potato"),getColor("potato"), 5)
            createBox("Carrot", getColor("carrot"), iron5Carrot)
            createBox("Potato", getColor("potato"), iron5Potato)
            st.markdown("<br>", unsafe_allow_html=True)
        elif switch == "Diamond Hoe":
            createName("Diamond Hoe", getColor("beetroot"),getColor("beetroot"), 1)
            createBox("Potato", getColor("potato"), diamond1Potato)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Diamond Hoe", getColor("beetroot"),getColor("beetroot"), 2)
            createBox("Potato", getColor("potato"), diamond2Potato)
            createBox("Beetroot", getColor("beetroot"), diamond2Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Diamond Hoe", getColor("beetroot"),getColor("beetroot"), 3)
            createBox("Beetroot", getColor("beetroot"), diamond3Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Diamond Hoe", getColor("beetroot"),getColor("beetroot"), 4)
            createBox("Wheat", getColor("wheat"), diamond4Wheat)
            createBox("Potato", getColor("potato"), diamond4Potato)
            createBox("Beetroot", getColor("beetroot"), diamond4Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Diamond Hoe", getColor("beetroot"),getColor("beetroot"), 5)
            createBox("Potato", getColor("potato"), diamond5Potato)
            createBox("Beetroot", getColor("beetroot"), diamond5Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
        elif switch == "Golden Hoe":
            createName("Golden Hoe", getColor("wheat"),getColor("wheat"), 1)
            createBox("Wheat", getColor("wheat"), golden1Wheat)
            createBox("Carrot", getColor("carrot"), golden1Carrot)
            createBox("Potato", getColor("potato"), golden1Potato)
            createBox("Beetroot", getColor("beetroot"), golden1Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Golden Hoe", getColor("wheat"),getColor("wheat"), 2)
            createBox("Potato", getColor("potato"), golden2Potato)
            createBox("Beetroot", getColor("beetroot"), golden2Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Golden Hoe", getColor("wheat"),getColor("wheat"), 3)
            createBox("Wheat", getColor("wheat"), golden3Wheat)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Golden Hoe", getColor("wheat"),getColor("wheat"), 4)
            createBox("Wheat", getColor("wheat"), golden4Wheat)
            createBox("Carrot", getColor("carrot"), golden4Carrot)
            createBox("Potato", getColor("potato"), golden4Potato)
            createBox("Beetroot", getColor("beetroot"), golden4Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Golden Hoe", getColor("wheat"),getColor("wheat"), 5)
            createBox("Wheat", getColor("wheat"), golden5Wheat)
            createBox("Carrot", getColor("carrot"), golden5Carrot)
            createBox("Potato", getColor("potato"), golden5Potato)
            createBox("Beetroot", getColor("beetroot"), golden5Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)

    elif type == "Iron Pickaxe [V]":

        beetrootTotal = formatNumber(700000 * num)
        coalTotal = formatNumber(1550000 * num)
        ironTotal = formatNumber(700000 * num)

        coal1Beetroot = formatNumber(500000 * num)
        coal2Coal = formatNumber(50000 * num)
        coal3Coal = formatNumber(150000 * num)
        coal4Coal = formatNumber(200000 * num)
        coal5Beetroot = formatNumber(200000 * num)
        coal5Coal = formatNumber(200000 * num)

        iron1Coal = formatNumber(500000 * num)
        iron2Iron = formatNumber(75000 * num)
        iron3Iron = formatNumber(175000 * num)
        iron4Coal = formatNumber(200000 * num)
        iron4Iron = formatNumber(200000 * num)
        iron5Coal = formatNumber(250000 * num)
        iron5Iron = formatNumber(250000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)


        createBox("Beetroot", getColor("beetroot"), beetrootTotal)
        createBox("Coal", getColor("coal"), coalTotal)
        createBox("Iron", getColor("iron"), ironTotal)

        st.divider()

        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Coal Pickaxe","Iron Pickaxe"]
        )

        if switch == "Coal Pickaxe":
            createName("Coal Pickaxe", getColor("coal"),getColor("coal"), 1)
            createBox("Beetroot", getColor("beetroot"), coal1Beetroot)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Coal Pickaxe", getColor("coal"),getColor("coal"), 2)
            createBox("Coal", getColor("coal"), coal2Coal)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Coal Pickaxe", getColor("coal"),getColor("coal"), 3)
            createBox("Coal", getColor("coal"), coal3Coal)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Coal Pickaxe", getColor("coal"),getColor("coal"), 4)
            createBox("Coal", getColor("coal"), coal4Coal)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Coal Pickaxe", getColor("coal"),getColor("coal"), 5)
            createBox("Beetroot", getColor("beetroot"), coal5Beetroot)
            createBox("Coal", getColor("coal"), coal5Coal)
            st.markdown("<br>", unsafe_allow_html=True)

        elif switch == "Iron Pickaxe":
            createName("Iron Pickaxe", getColor("iron"),getColor("iron"), 1)
            createBox("Coal", getColor("coal"), iron1Coal)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Pickaxe", getColor("iron"),getColor("iron"), 2)
            createBox("Iron", getColor("iron"), iron2Iron)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Pickaxe", getColor("iron"),getColor("iron"), 3)
            createBox("Iron", getColor("iron"), iron3Iron)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Pickaxe", getColor("iron"),getColor("iron"), 4)
            createBox("Coal", getColor("coal"), iron4Coal)
            createBox("Iron", getColor("iron"), iron4Iron)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Iron Pickaxe", getColor("iron"),getColor("iron"), 5)
            createBox("Coal", getColor("coal"), iron5Coal)
            createBox("Iron", getColor("iron"), iron5Iron)
            st.markdown("<br>", unsafe_allow_html=True)

    elif type == "Azure Extractor [V]":
        wheatTotal = formatNumber(7500000 * num)
        potatoTotal = formatNumber(7500000 * num)
        beetrootTotal = formatNumber(7500000 * num)
        spruceTotal = formatNumber(10500000 * num)
        cherryTotal = formatNumber(24000000 * num)
        auburnTotal = formatNumber(94500000 * num)
        carmineTotal = formatNumber(103500000 * num)
        ceruleanTotal = formatNumber(120750000 * num)
        azureTotal = formatNumber(73500000 * num)

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
        carmine5Auburn = formatNumber(10500000 * num)
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


        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)

        createBox("Wheat", getColor("wheat"), wheatTotal)
        createBox("Potato", getColor("potato"), potatoTotal)
        createBox("Beetroot", getColor("beetroot"), beetrootTotal)
        createBox("Spruce", getColor("spruce"), spruceTotal)
        createBox("Cherry", getColor("cherry"), cherryTotal)
        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Carmine Fungus", getColor("carmine"), carmineTotal)
        createBox("Cerulean Fungus", getColor("cerulean"), ceruleanTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        st.divider()

        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Auburn Extractor","Carmine Extractor","Cerulean Extractor","Azure Extractor"]
        )

        if switch == "Auburn Extractor":
            createName("Auburn Extractor", getColor("auburn"),getColor("auburn"), 1)
            createBox("Cherry", getColor("cherry"), auburn1Cherry)
            st.markdown("<br>", unsafe_allow_html=True)       
            createName("Auburn Extractor", getColor("auburn"),getColor("auburn"), 2)
            createBox("Auburn Roots", getColor("auburn"), auburn2Auburn)
            st.markdown("<br>", unsafe_allow_html=True)     
            createName("Auburn Extractor", getColor("auburn"),getColor("auburn"), 3)
            createBox("Auburn Roots", getColor("auburn"), auburn3Auburn)
            st.markdown("<br>", unsafe_allow_html=True)        
            createName("Auburn Extractor", getColor("auburn"),getColor("auburn"), 4)
            createBox("Auburn Roots", getColor("auburn"), auburn4Auburn)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Auburn Extractor", getColor("auburn"),getColor("auburn"), 5)
            createBox("Cherry", getColor("cherry"), auburn5Cherry)
            createBox("Auburn Roots", getColor("auburn"), auburn5Auburn)
            st.markdown("<br>", unsafe_allow_html=True)

        elif switch == "Carmine Extractor":
            createName("Carmine Extractor", getColor("carmine"),getColor("carmine"), 1)
            createBox("Spruce", getColor("spruce"), carmine1Spruce)
            createBox("Auburn Roots", getColor("auburn"), carmine1Auburn)
            st.markdown("<br>", unsafe_allow_html=True)       
            createName("Carmine Extractor", getColor("carmine"),getColor("carmine"), 2)
            createBox("Carmine Fungus", getColor("carmine"), carmine2Carmine)
            st.markdown("<br>", unsafe_allow_html=True)     
            createName("Carmine Extractor", getColor("carmine"),getColor("carmine"), 3)
            createBox("Carmine Fungus", getColor("carmine"), carmine3Carmine)
            st.markdown("<br>", unsafe_allow_html=True)        
            createName("Carmine Extractor", getColor("carmine"),getColor("carmine"), 4)
            createBox("Carmine Fungus", getColor("carmine"), carmine4Carmine)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Carmine Extractor", getColor("carmine"),getColor("carmine"), 5)
            createBox("Auburn Roots", getColor("auburn"), carmine5Auburn)
            createBox("Carmine Fungus", getColor("carmine"), carmine5Carmine)
            st.markdown("<br>", unsafe_allow_html=True)

        elif switch == "Cerulean Extractor":
            createName("Cerulean Extractor", getColor("cerulean"),getColor("cerulean"), 1)
            createBox("Wheat", getColor("wheat"), cerulean1Wheat)
            createBox("Potato", getColor("potato"), cerulean1Potato)
            createBox("Beetroot", getColor("beetroot"), cerulean1Beetroot)
            createBox("Carmine Fungus", getColor("carmine"), cerulean1Carmine)
            st.markdown("<br>", unsafe_allow_html=True)       
            createName("Cerulean Extractor", getColor("cerulean"),getColor("cerulean"), 2)
            createBox("Cerulean Fungus", getColor("cerulean"), cerulean2Cerulean)
            st.markdown("<br>", unsafe_allow_html=True)     
            createName("Cerulean Extractor", getColor("cerulean"),getColor("cerulean"), 3)
            createBox("Cerulean Fungus", getColor("cerulean"), cerulean3Cerulean)
            st.markdown("<br>", unsafe_allow_html=True)        
            createName("Cerulean Extractor", getColor("cerulean"),getColor("cerulean"), 4)
            createBox("Carmine Fungus", getColor("carmine"), cerulean4Carmine)
            createBox("Cerulean Fungus", getColor("cerulean"), cerulean4Cerulean)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Cerulean Extractor", getColor("cerulean"),getColor("cerulean"), 5)
            createBox("Cerulean Fungus", getColor("cerulean"), cerulean5Cerulean)
            st.markdown("<br>", unsafe_allow_html=True)

        elif switch == "Azure Extractor":
            createName("Azure Extractor", getColor("azure"),getColor("azure"), 1)
            createBox("Cerulean Fungus", getColor("carmine"), azure1Cerulean)
            st.markdown("<br>", unsafe_allow_html=True)       
            createName("Azure Extractor", getColor("azure"),getColor("azure"), 2)
            createBox("Cerulean Fungus", getColor("cerulean"), azure2Cerulean)
            createBox("Azure Roots", getColor("azure"), azure2Azure)
            st.markdown("<br>", unsafe_allow_html=True)     
            createName("Azure Extractor", getColor("azure"),getColor("azure"), 3)
            createBox("Azure Roots", getColor("azure"), azure3Azure)
            st.markdown("<br>", unsafe_allow_html=True)        
            createName("Azure Extractor", getColor("azure"),getColor("azure"), 4)
            createBox("Azure Roots", getColor("azure"), azure4Azure)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Azure Extractor", getColor("azure"),getColor("azure"), 5)
            createBox("Auburn Roots", getColor("auburn"), azure5Auburn)
            createBox("Carmine Fungus", getColor("carmine"), azure5Carmine)
            createBox("Cerulean Fungus", getColor("cerulean"), azure5Cerulean)
            createBox("Azure Roots", getColor("azure"), azure5Azure)
            st.markdown("<br>", unsafe_allow_html=True)

    elif type == "Twilight Scythe [V]":

        spruceTotal = formatNumber(75000000 * num)
        azureTotal = formatNumber(200000000 * num)
        twilightTotal = formatNumber(312500000 * num)

        twilight1Azure = formatNumber(200000000 * num)
        twilight2Twilight = formatNumber(25000000 * num)
        twilight3Twilight = formatNumber(62500000 * num)
        twilight4Twilight = formatNumber(100000000 * num)
        twilight5Spruce = formatNumber(75000000 * num)
        twilight5Twilight = formatNumber(125000000 * num)

        loc1,loc2,loc3,loc4,loc5 = st.columns([1,1,1,1,1])
        with loc3:
            st.markdown('<p style="white-space: nowrap; font-weight: bold;">Total Amount</p>', unsafe_allow_html=True)


        createBox("Spruce", getColor("spruce"), spruceTotal)
        createBox("Azure Roots", getColor("azure"), spruceTotal)
        createBox("Twilight Coral", getColor("twilight"), spruceTotal)

        st.divider()

        switch = st.selectbox(
            label = "nothing",
            label_visibility = "hidden",
            options = ["Twilight Scythe"]
        )

        if switch == "Twilight Scythe":
            createName("Twilight Scythe", getColor("twilight"),getColor("twilight"), 1)
            createBox("Azure Roots", getColor("azure"), twilight1Azure)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Twilight Scythe", getColor("twilight"),getColor("twilight"), 2)
            createBox("Twilight Coral", getColor("twilight"), twilight2Twilight)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Twilight Scythe", getColor("twilight"),getColor("twilight"), 3)
            createBox("Twilight Coral", getColor("twilight"), twilight3Twilight)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Twilight Scythe", getColor("twilight"),getColor("twilight"), 4)
            createBox("Twilight Coral", getColor("twilight"), twilight4Twilight)
            st.markdown("<br>", unsafe_allow_html=True)
            createName("Twilight Scythe", getColor("twilight"),getColor("twilight"), 5)
            createBox("Spruce", getColor("spruce"), twilight5Spruce)
            createBox("Twilight Coral", getColor("twilight"), twilight5Twilight)
            st.markdown("<br>", unsafe_allow_html=True)



st.divider()