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
        <div style="background-color: #gray; padding: 15px; border-radius: 12px; border: 1.6px solid {str};">
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



        st.divider()

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

        createBox("Auburn Roots", getColor("auburn"), auburnTotal)
        createBox("Azure Roots", getColor("azure"), azureTotal)
        createBox("Inferior Mushroom", getColor("inferior"), infTotal)
        createBox("Superior Mushroom", getColor("superior"), supTotal)
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
        st.divider()

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
        st.divider()


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
        st.divider()

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
        st.divider()


elif selector == "Toolmess":
    if type == "Extras":
        st.write("123")