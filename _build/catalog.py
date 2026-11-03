# Daily Stack catalogue data. Edit this file, then run: python3 _build/build.py
# claims = approved EU health claims (Regulation 432/2012). Keep the wording.
# pick = what's in our stacks today. compare = brands we look at for this product.

STACKS = {"foundation": "Foundation", "her": "Her", "energy": "Energy", "winter": "Winter"}

VM = ["Solgar", "NOW Foods", "Thorne", "Life Extension", "Pure Encapsulations", "Orthica", "Jarrow Formulas", "Vitakruid"]
HERB = ["NOW Foods", "Solgar", "Life Extension", "Jarrow Formulas", "Vitals", "Bonusan"]
SPORT = ["Mattisson Healthstyle", "NOW Foods", "Applied Nutrition", "BioTechUSA", "OstroVit", "Vitakruid"]

def c(group, slug, name, intro, claims=(), pick=None, compare=VM[:5], note=None):
    return dict(group=group, slug=slug, name=name, intro=intro, claims=list(claims), pick=pick, compare=list(compare), note=note)

CATEGORIES = [
# ---------- Vitamins ----------
c("Vitamins","multivitamin","Multivitamin","A broad base of vitamins and minerals in one product. Useful when you want to cover the basics without taking ten separate bottles.",
  ["Vitamin D contributes to the maintenance of normal bones.","Vitamin C contributes to the normal function of the immune system.","B vitamins contribute to normal energy-yielding metabolism."],
  pick=("Vitakruid","Multi Basis (30 tablets) · Multi Dag Vrouw in Her · Multi Dag Man Sport in Energy",["foundation","her","energy","winter"]),compare=["Vitakruid","Thorne","Pure Encapsulations","Solgar","Orthica"],
  note="Your vitamin D comes from the multivitamin, so you never double up on it."),
c("Vitamins","vitamin-a","Vitamin A","A fat-soluble vitamin found in liver, eggs and dairy, and made from beta-carotene in orange and green vegetables.",
  ["Vitamin A contributes to the maintenance of normal vision.","Vitamin A contributes to the maintenance of normal skin.","Vitamin A contributes to the normal function of the immune system."],
  note="Pregnant? Avoid high-dose vitamin A supplements unless your doctor advises them."),
c("Vitamins","vitamin-b-complex","Vitamin B complex","All eight B vitamins together. A practical choice for busy weeks, since the B vitamins work as a team in your metabolism.",
  ["Vitamin B6 and B12 contribute to the reduction of tiredness and fatigue.","Thiamine, riboflavin and niacin contribute to normal energy-yielding metabolism.","Vitamin B5 contributes to normal mental performance."],
  compare=["Thorne","Pure Encapsulations","Solgar","NOW Foods","Jarrow Formulas"]),
c("Vitamins","vitamin-b1","Vitamin B1 (thiamine)","Thiamine helps your body turn food into energy. Found in whole grains, pork, legumes and seeds.",
  ["Thiamine contributes to normal energy-yielding metabolism.","Thiamine contributes to the normal function of the heart.","Thiamine contributes to normal psychological function."]),
c("Vitamins","vitamin-b2","Vitamin B2 (riboflavin)","Riboflavin is found in dairy, eggs, meat and almonds. It gives many supplements their bright yellow colour.",
  ["Riboflavin contributes to the reduction of tiredness and fatigue.","Riboflavin contributes to the maintenance of normal vision.","Riboflavin contributes to the maintenance of normal skin."]),
c("Vitamins","vitamin-b3","Vitamin B3 (niacin)","Niacin comes in two common forms: nicotinic acid and niacinamide. Found in meat, fish, peanuts and whole grains.",
  ["Niacin contributes to the reduction of tiredness and fatigue.","Niacin contributes to the maintenance of normal skin.","Niacin contributes to normal psychological function."],
  note="High doses of the nicotinic acid form can cause a harmless but uncomfortable 'flush'."),
c("Vitamins","vitamin-b5","Vitamin B5 (pantothenic acid)","Pantothenic acid is found in almost all foods, from meat to mushrooms and avocado.",
  ["Pantothenic acid contributes to normal mental performance.","Pantothenic acid contributes to the reduction of tiredness and fatigue."]),
c("Vitamins","vitamin-b6","Vitamin B6 (pyridoxine)","Found in poultry, fish, potatoes, bananas and chickpeas. The active form is called P-5-P.",
  ["Vitamin B6 contributes to the normal function of the immune system.","Vitamin B6 contributes to the regulation of hormonal activity.","Vitamin B6 contributes to the reduction of tiredness and fatigue."],
  note="More is not better: stay within the dose on the label, as very high long-term doses of B6 can affect the nerves."),
c("Vitamins","biotin","Vitamin B8 (biotin)","Biotin is best known from hair and nail products. Found in eggs, nuts and seeds.",
  ["Biotin contributes to the maintenance of normal hair.","Biotin contributes to the maintenance of normal skin.","Biotin contributes to normal energy-yielding metabolism."],
  note="Biotin can disturb some blood tests. Tell your doctor or lab if you take it."),
c("Vitamins","folic-acid","Vitamin B11 (folate)","Folate is found in leafy greens and legumes. Many women take it when trying to get pregnant. Methylfolate is the active form.",
  ["Supplemental folic acid intake increases maternal folate status.","Folate contributes to maternal tissue growth during pregnancy.","Folate contributes to the reduction of tiredness and fatigue."]),
c("Vitamins","vitamin-b12","Vitamin B12","B12 comes almost only from animal foods, which makes it the number one supplement for vegetarians and vegans. Methylcobalamin is a popular active form.",
  ["Vitamin B12 contributes to normal red blood cell formation.","Vitamin B12 contributes to the reduction of tiredness and fatigue.","Vitamin B12 contributes to the normal function of the immune system."],
  pick=("Solgar","Methylcobalamin 1000 µg (30 nuggets)",["her"]),compare=["Solgar","Pure Encapsulations","Jarrow Formulas","Thorne","NOW Foods"]),
c("Vitamins","vitamin-c","Vitamin C","The classic. Found in citrus, peppers and kiwi. A buffered form is gentler on the stomach than plain ascorbic acid.",
  ["Vitamin C contributes to the normal function of the immune system.","Vitamin C contributes to normal collagen formation for the normal function of skin.","Vitamin C increases iron absorption."],
  pick=("Bonusan","Vitamine C-1000 (30 tablets)",["foundation","her","energy","winter"]),compare=["Solgar","Pure Encapsulations","Bonusan","Vitakruid","Orthica"]),
c("Vitamins","vitamin-d3","Vitamin D3","In winter the sun in most of Europe is too weak to make enough vitamin D in your skin. That's why it's one of the most taken supplements across the EU.",
  ["Vitamin D contributes to the maintenance of normal bones.","Vitamin D contributes to the normal function of the immune system.","Vitamin D contributes to the maintenance of normal muscle function."],
  pick=("Vitakruid","in your multivitamin (Multi Basis, Multi Dag Vrouw, Multi Dag Man Sport)",["foundation","her","energy","winter"]),compare=["Nordic Naturals","Sunday Natural","Solgar","Orthica","Vitakruid"],
  note="The Dutch Health Council advises extra vitamin D for many groups, including everyone over 70 and people who get little sun."),
c("Vitamins","vitamin-e","Vitamin E","A fat-soluble vitamin found in nuts, seeds and plant oils. Look for mixed tocopherols.",
  ["Vitamin E contributes to the protection of cells from oxidative stress."]),
c("Vitamins","vitamin-k2","Vitamin K2","K2 (as MK-7) is often paired with vitamin D3. Found in fermented foods like natto and in some cheeses.",
  ["Vitamin K contributes to the maintenance of normal bones.","Vitamin K contributes to normal blood clotting."],
  compare=["Sunday Natural","Life Extension","Jarrow Formulas","Solgar","Vitakruid"],
  note="Using blood thinners such as warfarin or acenocoumarol? Do not take vitamin K without talking to your doctor."),
# ---------- Minerals ----------
c("Minerals","magnesium","Magnesium","One of Europe's most popular supplements. Glycinate is a gentle, well-absorbed form that's easy on the stomach.",
  ["Magnesium contributes to the reduction of tiredness and fatigue.","Magnesium contributes to normal muscle function.","Magnesium contributes to normal psychological function."],
  pick=("Vitakruid","Magnesium 200 Complex (30 tablets)",["foundation","her","energy","winter"]),compare=["Pure Encapsulations","Thorne","Solgar","NOW Foods","Vitakruid"]),
c("Minerals","zinc","Zinc","Found in meat, shellfish, seeds and legumes. Picolinate and bisglycinate are well-absorbed forms.",
  ["Zinc contributes to the normal function of the immune system.","Zinc contributes to the maintenance of normal skin.","Zinc contributes to the maintenance of normal hair and nails."],
  compare=["Solgar","Thorne","Pure Encapsulations","NOW Foods","Orthica"]),
c("Minerals","selenium","Selenium","A trace mineral found in Brazil nuts, fish and eggs. European soils are low in selenium.",
  ["Selenium contributes to the normal function of the immune system.","Selenium contributes to normal thyroid function.","Selenium contributes to the maintenance of normal hair and nails."],
  compare=["Solgar","NOW Foods","Pure Encapsulations","Life Extension","Orthica"]),
c("Minerals","iron","Iron","Found in red meat, legumes and leafy greens. Many women need more iron, especially with heavy periods.",
  ["Iron contributes to normal formation of red blood cells and haemoglobin.","Iron contributes to the reduction of tiredness and fatigue.","Iron contributes to normal cognitive function."],
  note="Only take iron if you need it; a blood test tells you. Keep iron supplements away from children."),
c("Minerals","calcium","Calcium","The main building block of bones and teeth. Found in dairy, leafy greens and fortified plant drinks.",
  ["Calcium is needed for the maintenance of normal bones.","Calcium is needed for the maintenance of normal teeth.","Calcium contributes to normal muscle function."]),
c("Minerals","potassium","Potassium","Found in potatoes, bananas, beans and vegetables. Most people get it from food.",
  ["Potassium contributes to normal muscle function.","Potassium contributes to the maintenance of normal blood pressure."],
  note="Have kidney problems or take blood pressure medication? Ask your doctor before taking potassium."),
c("Minerals","iodine","Iodine","Iodine is added to bread salt in the Netherlands. Found in fish, seaweed and dairy.",
  ["Iodine contributes to normal thyroid function.","Iodine contributes to normal cognitive function.","Iodine contributes to the maintenance of normal skin."],
  note="Have a thyroid condition? Talk to your doctor before taking iodine."),
c("Minerals","chromium","Chromium","A trace mineral found in broccoli, whole grains and meat.",
  ["Chromium contributes to the maintenance of normal blood glucose levels.","Chromium contributes to normal macronutrient metabolism."]),
# ---------- Supplements ----------
c("Supplements","omega-3","Omega-3 &amp; fish oil","EPA and DHA from fish oil. Most people eat less oily fish than the recommended once a week, which makes omega-3 a staple in every one of our stacks.",
  ["EPA and DHA contribute to the normal function of the heart (with a daily intake of 250 mg EPA and DHA).","DHA contributes to the maintenance of normal brain function (250 mg DHA per day).","DHA contributes to the maintenance of normal vision (250 mg DHA per day)."],
  pick=("Bonusan","Omega-3 DHA Forte (30 softgels)",["foundation","her","energy","winter"]),compare=["Nordic Naturals","Norsan","Solgar","Bonusan","Vitakruid"]),
c("Supplements","collagen","Collagen","Collagen peptides are protein fragments, usually from beef or fish, that mix easily into coffee or a smoothie.",
  [],compare=["NOW Foods","Vital Proteins","Solgar","Jarrow Formulas","Applied Nutrition"],
  note="There are no approved EU health claims for collagen itself. Vitamin C contributes to normal collagen formation for the normal function of skin."),
c("Supplements","probiotics","Probiotics","Live bacteria, usually Lactobacillus and Bifidobacterium strains, in capsules or powders. Orthica is one of the best-known Dutch brands.",pick=("Orthica","Orthiflor Original (30 capsules)",["foundation","her","winter"]),compare=["Orthica","Jarrow Formulas","Bonusan","Solgar","NOW Foods"]),
c("Supplements","prebiotics","Prebiotics","Fibres such as inulin and FOS that feed the bacteria already living in your gut.",compare=["NOW Foods","Jarrow Formulas","Bonusan","Solgar","Life Extension"]),
c("Supplements","coq10","CoQ10","Coenzyme Q10, a compound your body makes itself. Available as ubiquinone and ubiquinol.",compare=["Life Extension","Pure Encapsulations","Solgar","NOW Foods","Jarrow Formulas"],
  note="Taking statins or blood thinners? Ask your doctor first."),
c("Supplements","protein","Protein","Protein powders from whey, casein, pea or rice. Handy after training or for an easy breakfast.",
  ["Protein contributes to a growth in muscle mass.","Protein contributes to the maintenance of muscle mass.","Protein contributes to the maintenance of normal bones."],compare=SPORT[:5]),
c("Supplements","amino-acids","Amino acids","The building blocks of protein, sold as single amino acids or blends.",compare=["NOW Foods","Solgar","Jarrow Formulas","Applied Nutrition","OstroVit"]),
c("Supplements","antioxidants","Antioxidants","A broad group that includes vitamin C, vitamin E, selenium and plant compounds.",
  ["Vitamin C, vitamin E and selenium contribute to the protection of cells from oxidative stress."],compare=VM[:5]),
c("Supplements","astaxanthin","Astaxanthin","A red pigment from algae. It's what makes salmon and flamingos pink.",compare=["NOW Foods","Life Extension","Jarrow Formulas","Solgar","Vitals"]),
c("Supplements","colostrum","Colostrum","The first milk produced by cows after giving birth, sold as a powder or capsules.",compare=["Applied Nutrition","NOW Foods","Life Extension","Solgar","Vitals"]),
c("Supplements","enzymes","Digestive enzymes","Enzymes like amylase, protease and lipase that help break down food.",compare=["NOW Foods","Pure Encapsulations","Solgar","Jarrow Formulas","Life Extension"]),
c("Supplements","glucosamine","Glucosamine","Often combined with chondroitin or MSM. Usually made from shellfish.",compare=["Solgar","NOW Foods","Life Extension","Jarrow Formulas","Vitals"],
  note="Allergic to shellfish? Choose a vegan glucosamine."),
c("Supplements","inositol","Inositol","A sugar-like compound, often sold as myo-inositol powder.",compare=["NOW Foods","Jarrow Formulas","Solgar","Pure Encapsulations","Life Extension"]),
c("Supplements","lutein","Lutein","A yellow pigment found in kale, spinach and egg yolk, often combined with zeaxanthin.",compare=["Solgar","NOW Foods","Life Extension","Jarrow Formulas","Vitals"]),
c("Supplements","melatonin","Melatonin","A hormone your body makes in the evening. Popular for jet lag.",compare=["Vitals","Solgar","NOW Foods","Vitakruid","Life Extension"],
  note="In the Netherlands, supplements may contain up to 0.3 mg melatonin; higher doses count as medicine."),
c("Supplements","msm","MSM","Methylsulfonylmethane, a natural sulphur compound, often combined with glucosamine.",compare=["NOW Foods","Solgar","Jarrow Formulas","Life Extension","Vitals"]),
c("Supplements","quercetin","Quercetin","A plant compound found in onions, apples and capers.",compare=["NOW Foods","Solgar","Life Extension","Jarrow Formulas","Pure Encapsulations"]),
c("Supplements","resveratrol","Resveratrol","A compound found in grape skins and Japanese knotweed.",compare=["Life Extension","NOW Foods","Solgar","Jarrow Formulas","Pure Encapsulations"]),
c("Supplements","taurine","Taurine","An amino acid found in meat and fish, and in many energy drinks.",compare=["NOW Foods","Solgar","Life Extension","Jarrow Formulas","OstroVit"]),
c("Supplements","5-htp","5-HTP","Made from the seeds of the Griffonia plant.",compare=["NOW Foods","Solgar","Life Extension","Jarrow Formulas","Vitals"],
  note="Do not combine 5-HTP with antidepressants or other medication without your doctor's advice."),
# ---------- Herbs & plants ----------
c("Herbs &amp; plants","ashwagandha","Ashwagandha","A root used in Ayurveda for centuries, often sold as KSM-66 extract.",compare=HERB[:5],
  note="Pregnant, or have a thyroid condition? Ask your doctor before using ashwagandha."),
c("Herbs &amp; plants","turmeric","Turmeric (curcuma)","The golden spice, usually combined with black pepper (piperine).",compare=HERB[:5],
  note="Using blood thinners? Ask your doctor first."),
c("Herbs &amp; plants","rhodiola","Rhodiola","A root from cold mountain regions, also called golden root.",compare=HERB[:5]),
c("Herbs &amp; plants","ginseng","Ginseng","Asian (Panax) ginseng root, one of the best-known traditional herbs.",compare=HERB[:5]),
c("Herbs &amp; plants","maca","Maca","A root from the Andes, usually sold as a powder.",compare=HERB[:5]),
c("Herbs &amp; plants","ginkgo","Ginkgo biloba","An extract from the leaves of the ginkgo tree.",compare=HERB[:5],note="Using blood thinners? Ask your doctor first."),
c("Herbs &amp; plants","echinacea","Echinacea","A purple coneflower, popular in winter.",compare=HERB[:5]),
c("Herbs &amp; plants","elderberry","Elderberry","Black elderberry, often sold as a syrup or gummy.",compare=HERB[:5]),
c("Herbs &amp; plants","cranberry","Cranberry","Cranberry extract in capsules, an easy alternative to the juice.",compare=HERB[:5]),
c("Herbs &amp; plants","boswellia","Boswellia","Resin from the frankincense tree.",compare=HERB[:5]),
c("Herbs &amp; plants","milk-thistle","Milk thistle","Seeds of the milk thistle plant, standardised for silymarin.",compare=HERB[:5]),
c("Herbs &amp; plants","saffron","Saffron","An extract of the world's most expensive spice.",compare=HERB[:5]),
c("Herbs &amp; plants","spirulina","Spirulina","Blue-green algae in tablets or powder.",compare=HERB[:5]),
c("Herbs &amp; plants","chlorella","Chlorella","Green freshwater algae in tablets or powder.",compare=HERB[:5]),
c("Herbs &amp; plants","garlic","Garlic","Odourless garlic extract in capsules.",compare=HERB[:5],note="Using blood thinners? Ask your doctor first."),
c("Herbs &amp; plants","valerian","Valerian","A root traditionally used in the evening.",compare=HERB[:5]),
# ---------- Sport ----------
c("Sport","creatine","Creatine","One of the most researched sports supplements. Creapure® is a German-made, high-purity creatine monohydrate.",
  ["Creatine increases physical performance in successive bursts of short-term, high-intensity exercise (with a daily intake of 3 g)."],
  pick=("Mattisson Healthstyle","Creatine Creapure® capsules (180 = 30 days)",["energy"]),compare=SPORT[:5]),
c("Sport","electrolytes","Electrolytes","Sodium, potassium and magnesium to mix into water, for long training sessions or hot days.",
  ["Carbohydrate-electrolyte solutions contribute to the maintenance of endurance performance during prolonged endurance exercise.","Carbohydrate-electrolyte solutions enhance the absorption of water during physical exercise."],
  compare=["NOW Foods","Applied Nutrition","Salte","BioTechUSA","OstroVit"]),
c("Sport","protein-bars","Protein bars","A quick snack with extra protein, for after training or on the go.",
  ["Protein contributes to a growth in muscle mass."],compare=SPORT[:5]),
c("Sport","energy-gels","Energy gels","Fast carbohydrates in a small pouch, for long runs and rides.",
  ["Carbohydrate-electrolyte solutions contribute to the maintenance of endurance performance during prolonged endurance exercise."],compare=SPORT[:5]),
c("Sport","pre-workout","Pre-workout","Blends taken before training, often with caffeine.",compare=SPORT[:5],
  note="Most pre-workouts contain caffeine. Not suitable for children, or if you're pregnant or caffeine-sensitive."),
c("Sport","post-workout","Post-workout","Recovery blends, usually protein with carbohydrates.",["Protein contributes to a growth in muscle mass."],compare=SPORT[:5]),
c("Sport","green-tea","Green tea extract","Concentrated green tea, often standardised for EGCG.",compare=HERB[:5],
  note="Take with food and stay within the label dose."),
c("Sport","bcaa","BCAA","The branched-chain amino acids leucine, isoleucine and valine.",compare=SPORT[:5]),
c("Sport","carnitine","Carnitine","L-carnitine, an amino acid derivative popular in sports nutrition.",compare=SPORT[:5]),
c("Sport","glutamine","L-Glutamine","The most common amino acid in your muscles, usually sold as a powder.",compare=SPORT[:5]),
]

# Evidence standard: we only list products with an approved EU health claim (A),
# or with promising human trials that we describe honestly (B: probiotics, prebiotics, CoQ10, echinacea, rhodiola, ginseng, cranberry).
# Everything below failed that test (weak or industry-only evidence, or safety concerns), so it is not in our box.
NOT_IN_OUR_BOX = {
  "collagen": "Independent, high-quality studies have not shown an effect on the skin.",
  "melatonin": "Dutch supplements are capped at 0.3 mg, below the dose the approved claim needs.",
  "ashwagandha": "Not included because of safety concerns; Denmark has banned it in supplements.",
  "turmeric": "No approved claim, and reports of liver injury from strong extracts.",
  "valerian": "Weak evidence.",
  "amino-acids": "Not needed with an adequate protein intake.",
  "bcaa": "Not needed with an adequate protein intake.",
  "glutamine": "No good evidence for healthy people.",
  "carnitine": "No good evidence for healthy people.",
  "pre-workout": "Mostly caffeine blends with ingredients that lack evidence.",
  "green-tea": "Reports of liver injury from concentrated extracts.",
  "5-htp": "Risky interactions with medication.",
  "resveratrol": "No solid human evidence.",
  "quercetin": "No solid human evidence.",
  "astaxanthin": "No solid human evidence.",
  "colostrum": "No solid human evidence.",
  "enzymes": "No solid evidence for healthy people.",
  "glucosamine": "Large independent trials found little or no effect.",
  "msm": "No solid human evidence.",
  "inositol": "Evidence only for specific medical conditions.",
  "lutein": "Evidence only for people with eye disease.",
  "taurine": "No solid human evidence.",
  "maca": "No solid human evidence.",
  "ginkgo": "A large trial found no effect on memory.",
  "elderberry": "Weak evidence.",
  "boswellia": "Weak evidence.",
  "milk-thistle": "Weak evidence.",
  "saffron": "Small trials only.",
  "spirulina": "No solid human evidence.",
  "chlorella": "No solid human evidence.",
  "garlic": "Small effects, and interacts with blood thinners.",
  "echinacea": "A.Vogel Echinaforce drops are registered as a medicine in the Netherlands; selling them needs a drugstore licence.",
}
# Single B vitamins are covered by the B complex, so we don't list them separately.
COVERED_BY_B_COMPLEX = {"vitamin-b1", "vitamin-b2", "vitamin-b5", "vitamin-b6"}
# Low demand, so we don't list them as add-ons. People can still request them.
LOW_DEMAND = {"rhodiola", "ginseng", "potassium", "chromium"}
CATEGORIES = [x for x in CATEGORIES if x["slug"] not in NOT_IN_OUR_BOX and x["slug"] not in COVERED_BY_B_COMPLEX and x["slug"] not in LOW_DEMAND]

# Evidence grade per product.
# A = approved EU health claim + solid human research. B = no approved claim or early/small trials; we say so plainly.
GRADE_B = {
  "probiotics": "No approved EU health claim yet. Effects depend on the specific strain, and research is still developing. We review this grade as new research is published.",
  "prebiotics": "Chicory inulin has an approved EU health claim at 12 g per day. At lower amounts the evidence is still developing. We review this grade as new research is published.",
  "coq10": "No approved EU health claim yet. The body produces CoQ10 itself, and studies in healthy adults are still limited. We review this grade as new research is published.",
  "antioxidants": "Vitamin C, vitamin E and selenium in this product have approved EU health claims. The added plant extracts do not yet. We review this grade as new research is published.",
  "cranberry": "No approved EU health claim yet, and the human research is still developing. We review this grade as new research is published.",
}
GRADE_A_NOTE = "Approved EU health claim, supported by human research."
def grade(slug): return "B" if slug in GRADE_B else "A"

# Add-ons: the product we put in your box when you add this to your stack. (brand, product, photo in assets/products)
ADDON = {
  "vitamin-a": ("Vitakruid", "Vitamine A 4000 IE Vegan", "vitakruid-vitamin-a"),
  "vitamin-b-complex": ("Vitakruid", "B-Complex Actief", "vitakruid-b-complex"),
  "vitamin-b3": ("Vitakruid", "Vitamine B3 Niacinamide 500 mg", "vitakruid-b3"),
  "folic-acid": ("Vitakruid", "Actief Foliumzuur 400 mcg", "vitakruid-folic-acid"),
  "vitamin-e": ("Vitakruid", "Vitamine E 230 TE Complex", "vitakruid-vitamin-e"),
  "vitamin-k2": ("Vitakruid", "Vitamine K2 &amp; D3 drops", "vitakruid-k2-d3"),
  "zinc": ("Vitakruid", "Zink-Methionine &amp; Koper", "vitakruid-zinc"),
  "antioxidants": ("Bonusan", "Santiox", "bonusan-santiox"),
  "selenium": ("Pharma Nord", "Bio-Selenium + Zinc", "pharmanord-selenium"),
  "iron": ("Vitakruid", "IJzer Bisglycinaat Complex", "vitakruid-iron"),
  "calcium": ("Vitakruid", "Calcium 400 &amp; D3 uit Rode Alg", "vitakruid-calcium"),
  "iodine": ("Vitakruid", "Jodium drops", "vitakruid-iodine"),
  "prebiotics": ("Bonusan", "FibroPur Inuline FOS", "bonusan-fibropur"),
  "coq10": ("Pharma Nord", "Bio-Qinon Active Q10 Gold 100 mg", "pharmanord-q10"),
  "cranberry": ("A.Vogel", "Cranberry Complex", "avogel-cranberry"),
  "electrolytes": ("XXL Nutrition", "Electrolytes", "xxl-electrolytes"),
  "protein-bars": ("XXL Nutrition", "High Protein Bar", "xxl-protein-bar"),
  "energy-gels": ("XXL Nutrition", "Energy Gel Pro", "xxl-energy-gel"),
  "post-workout": ("XXL Nutrition", "Muscle Grow (post-workout)", "xxl-muscle-grow"),
}
# Add-ons without their own product page.
ADDON_EXTRA = {
  "d3": ("Vitakruid", "Vitamine D3 Vegan 25 mcg", "vitakruid-d3", "Vitamin D3"),
  "kids-d": ("Davitamon", "Baby vitamine K + D drops", "davitamon-baby-kd", "Kids' vitamin D"),
  "algae-omega3": ("Bonusan", "Omega-3 algae oil (vegan)", "bonusan-algae-omega3", "Vegan omega-3"),
}
# DRAFT monthly add-on prices in euro cents (30-day pack, around shelf price). TODO: check against real shelf prices.
ADDON_PRICE = {
  "d3": 695, "kids-d": 995, "algae-omega3": 2495, "folic-acid": 695, "iron": 895, "zinc": 995, "iodine": 895,
  "vitamin-a": 795, "vitamin-b-complex": 995, "vitamin-b3": 795, "vitamin-e": 995, "vitamin-k2": 1295,
  "selenium": 1495, "calcium": 795, "prebiotics": 1295, "coq10": 2795, "antioxidants": 1995,
  "echinacea": 1195, "cranberry": 1295, "electrolytes": 1495, "protein-bars": 2495, "energy-gels": 1995, "post-workout": 2995,
}
# Suggested extras in the box drawer, per stack.
SUGGEST = {
  "foundation": ["d3", "prebiotics", "zinc", "algae-omega3"],
  "her": ["iron", "folic-acid", "d3", "zinc"],
  "energy": ["electrolytes", "protein-bars", "d3", "coq10"],
  "winter": ["d3", "zinc", "cranberry"],
}

# Menu groups (order shown in the menu)
MENU = {
  "vit": ("Vitamins &amp; supplements", [("Vitamins",[x for x in CATEGORIES if x["group"]=="Vitamins"],""),
                                          ("Minerals",[x for x in CATEGORIES if x["group"]=="Minerals"],""),
                                          ("Supplements",[x for x in CATEGORIES if x["group"]=="Supplements"],"span2"),
                                          ("Herbs &amp; plants",[x for x in CATEGORIES if x["group"]=="Herbs &amp; plants"],"")]),
}

# Local brands: mostly Dutch, all sold in Dutch drugstores and pharmacies (Etos, Kruidvat, De Online Drogist, Vitaminstore).
LOCAL = {
  "Vitamins": ["Vitakruid","Bonusan","Orthica","Lucovitaal","Proviform","Vitals","AOV","Davitamon","Solgar"],
  "Minerals": ["Vitakruid","Orthica","Bonusan","Lucovitaal","Proviform","Golden Naturals","AOV"],
  "Supplements": ["Bonusan","Orthica","Vitakruid","Vitals","Lucovitaal","Golden Naturals","Energetica Natura"],
  "Herbs &amp; plants": ["A.Vogel","Bonusan","Vitakruid","Lucovitaal","Golden Naturals","Arkopharma","Ortholon"],
  "Sport": ["Mattisson Healthstyle","XXL Nutrition","Body &amp; Fit","Vitakruid","Bonusan"],
}
LOCAL_OVR = {
  "multivitamin": ["Vitakruid","Orthica","Davitamon","Lucovitaal","Vitals"],
  "vitamin-c": ["Bonusan","Orthica","Vitakruid","Roter","Lucovitaal"],
  "vitamin-d3": ["Vitakruid","Davitamon","Lucovitaal","Orthica","Bonusan"],
  "selenium": ["Pharma Nord","Orthica","Bonusan","Vitakruid","Lucovitaal"],
  "omega-3": ["Bonusan","Vitakruid","Orthica","Vitals","Lucovitaal"],
  "probiotics": ["Orthica","Vitals","Bonusan","Lucovitaal","Golden Naturals"],
  "collagen": ["Energetica Natura","Vitakruid","Lucovitaal","Body &amp; Fit","XXL Nutrition"],
  "coq10": ["Pharma Nord","Bonusan","Vitakruid","Orthica","Lucovitaal"],
  "protein": ["XXL Nutrition","Body &amp; Fit","Mattisson Healthstyle","Vitakruid"],
  "amino-acids": ["XXL Nutrition","Body &amp; Fit","Proviform","Bonusan"],
  "melatonin": ["Vitals","Lucovitaal","Vitakruid","Davitamon"],
  "echinacea": ["A.Vogel","Lucovitaal","Bonusan","Arkopharma"],
  "valerian": ["A.Vogel","Lucovitaal","Arkopharma","Vitakruid"],
  "green-tea": ["A.Vogel","Lucovitaal","Golden Naturals","Bonusan"],
  "electrolytes": ["XXL Nutrition","Body &amp; Fit","Mattisson Healthstyle","Vitakruid"],
  "creatine": ["Mattisson Healthstyle","XXL Nutrition","Body &amp; Fit","Vitakruid"],
}
for _c in CATEGORIES:
    _l = list(LOCAL_OVR.get(_c["slug"], LOCAL[_c["group"]]))
    _a = ADDON.get(_c["slug"])
    if _a and not _c["pick"]:
        if _a[0] in _l: _l.remove(_a[0])
        _l.insert(0, _a[0])
    if _c["pick"] and _c["pick"][0] in _l: _l.remove(_c["pick"][0])
    if _c["pick"]: _l.insert(0, _c["pick"][0])
    _c["compare"] = _l[:5]

TOP_BRANDS = ["Vitakruid","Bonusan","Orthica","Lucovitaal","Solgar","Mattisson Healthstyle","XXL Nutrition"]
SPORT_BRANDS = ["Mattisson Healthstyle","XXL Nutrition","Body &amp; Fit","Vitakruid","Bonusan"]
# Only brands we actually list for a product (no empty brand cards).
ALL_BRANDS = sorted(set(sum((_c["compare"] for _c in CATEGORIES), []) + TOP_BRANDS), key=str.lower)

# ---------------- Stacks (plan pages at /stack/<id>) ----------------
# Every product is a 30-day pack, so each box is exactly one month.
# item = (label, brand, product, pack (what a 30-day pack is), category slug or None, photo name in assets/products or None)
STRIPE = {
  "foundation": "https://buy.stripe.com/test_00weVedkR8p3aUI31f97G05",
  "her": "https://buy.stripe.com/test_7sY8wQa8F0WB7Iw45j97G06",
  "energy": "https://buy.stripe.com/test_eVq8wQ80xbBfgf26dr97G07",
  "winter": "https://buy.stripe.com/test_6oU14o3Khaxb9QE31f97G08",
}
BRAND_LOGO = {"Nordic Naturals": "nordic-naturals", "Pure Encapsulations": "pure-encapsulations", "Solgar": "solgar", "Vitakruid": "vitakruid",
              "Mattisson Healthstyle": "mattisson", "NOW Foods": "now-foods", "Orthica": "orthica", "Bonusan": "bonusan", "Daily Stack": None}
OMEGA = ("Omega-3", "Bonusan", "Omega-3 DHA Forte", "30 softgels · 1 a day", "omega-3", "bonusan-omega3")
MAG = ("Magnesium", "Vitakruid", "Magnesium 200 Complex", "30 tablets · 1 a day", "magnesium", "vitakruid-magnesium")
VITC = ("Vitamin C", "Bonusan", "Vitamine C-1000", "30 tablets · 1 a day", "vitamin-c", "bonusan-c1000")
MULTI = ("Multivitamin", "Vitakruid", "Multi Basis", "30 tablets · 1 a day", "multivitamin", "vitakruid-multi-basis")
FLORA = ("Probiotic", "Orthica", "Orthiflor Original", "30 capsules · 1 a day", "probiotics", "orthica-orthiflor")  # TODO: placeholder photo (Dino Orthiflor), replace with Orthiflor Original
CREA = ("Creatine", "Mattisson Healthstyle", "Creatine Creapure® capsules", "180 vegicaps · 6 a day (3 g)", "creatine", "mattisson-creatine")
DISCOVERY = ("Monthly discovery", "Daily Stack", "A new product to try, picked by us", "1 product a month", None, None)
STACK_LIST = [
  dict(id="foundation", name="Foundation", price="€109", per="/ month · free shipping", badge="Most popular",
       tagline="Essential daily nutrients for adults. 5 products, plus a new addition each month.",
       items=[MULTI, OMEGA, MAG, VITC, FLORA, DISCOVERY],
       extras=["Weekly pill organizer (first box)", "Your daily schedule", "A \"why this brand\" card for every product"], cta="Subscribe to Foundation"),
  dict(id="her", name="Her", price="€129", per="/ month · free shipping", badge=None,
       tagline="Made for women: a women's multi, plus B12. 6 products.",
       items=[("Women's multivitamin", "Vitakruid", "Multi Dag Vrouw", "30 tablets · 1 a day", "multivitamin", "vitakruid-multi-vrouw"), OMEGA, MAG,
              ("Vitamin B12", "Solgar", "Methylcobalamin 1000 µg", "30 nuggets · 1 a day", "vitamin-b12", "solgar-b12"), VITC, FLORA],
       extras=["Pill organizer (first box)", "Your daily schedule", "A \"why this brand\" card for every product"], cta="Subscribe to Her Stack"),
  dict(id="energy", name="Energy", price="€129", per="/ month · free shipping", badge=None,
       tagline="For active adults, with creatine for training. 6 products.",
       items=[("Sport multivitamin", "Vitakruid", "Multi Dag Man Sport", "30 tablets · 1 a day", "multivitamin", "vitakruid-multi-sport"), OMEGA, MAG, CREA, VITC, FLORA],
       extras=["Shaker (first box)", "Pill organizer (first box)", "Training-day schedule"], cta="Subscribe to Energy Stack"),
  dict(id="winter", name="Winter", price="€109", per="one-time · free shipping", badge="Christmas gift",
       tagline="For the winter months: 5 products, plus tea, honey and lip balm.",
       items=[VITC, MULTI, OMEGA, MAG, FLORA],
       extras=["Ginger-lemon tea", "Dutch honey", "Lip balm", "Gift card"], cta="Order the Winter Stack", note="Order before 15 December for delivery before Christmas."),
]
