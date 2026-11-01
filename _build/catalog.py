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

# Menu groups (order shown in the menu)
MENU = {
  "vit": ("Vitamins &amp; supplements", [("Vitamins",[x for x in CATEGORIES if x["group"]=="Vitamins"],""),
                                          ("Minerals",[x for x in CATEGORIES if x["group"]=="Minerals"],""),
                                          ("Supplements",[x for x in CATEGORIES if x["group"]=="Supplements"],"span2"),
                                          ("Herbs &amp; plants",[x for x in CATEGORIES if x["group"]=="Herbs &amp; plants"],"")]),
}

TOP_BRANDS = ["Nordic Naturals","Pure Encapsulations","Solgar","Vitakruid","Orthica","Mattisson Healthstyle","NOW Foods"]
ALL_BRANDS = sorted(set(["21st Century","Absonutrix","Allergy Research Group","Applied Nutrition","BioTechUSA","Blueprint","Bon Charge","Bonusan","Codeage","EuroVital","Foligain","Goli Nutrition","H2Tab","Jarrow Formulas","Kiki Health","Laveen","Life Extension","Lindens","Linn Pharma","Natrol","Nature's Answer","NatureWise","Newton-Everett","Nordic Naturals","Norsan","NOW Foods","Optimox","OstroVit","ProHealth Longevity","Quicksilver","Salte","Solgar","SuperFeast","Swanson","Ten Percent Club","Trace Minerals","Viridian","Vitakruid","Vitalized","Vitals","Vuzïmo","Watermans","Yummygums","Zooki","Pure Encapsulations","Thorne","Mattisson Healthstyle","Sunday Natural","Orthica","Garden of Life","Doppelherz","Orthomol","Vital Proteins","Bonusan"]), key=str.lower)

# ---------------- Stacks (plan pages at /stack/<id>) ----------------
# Every product is a 30-day pack, so each box is exactly one month.
# item = (label, brand, product, pack (what a 30-day pack is), category slug or None, photo name in assets/products or None)
STRIPE = {
  "foundation": "https://buy.stripe.com/test_00weVedkR8p3aUI31f97G05",
  "her": "https://buy.stripe.com/test_7sY8wQa8F0WB7Iw45j97G06",
  "energy": "https://buy.stripe.com/test_aFa4gA6Wt9t72oc8lz97G02",
  "winter": "https://buy.stripe.com/test_6oUdRa80x48N2ocdFT97G01",
}
BRAND_LOGO = {"Nordic Naturals": "nordic-naturals", "Pure Encapsulations": "pure-encapsulations", "Solgar": "solgar", "Vitakruid": "vitakruid",
              "Mattisson Healthstyle": "mattisson", "NOW Foods": "now-foods", "Orthica": None, "Daily Stack": None}
OMEGA = ("Omega-3", "Bonusan", "Omega-3 DHA Forte", "30 softgels · 1 a day", "omega-3", None)
MAG = ("Magnesium", "Vitakruid", "Magnesium 200 Complex", "30 tablets · 1 a day", "magnesium", None)
VITC = ("Vitamin C", "Bonusan", "Vitamine C-1000", "30 tablets · 1 a day", "vitamin-c", None)
MULTI = ("Multivitamin", "Vitakruid", "Multi Basis", "30 tablets · 1 a day", "multivitamin", None)
FLORA = ("Probiotic", "Orthica", "Orthiflor Original", "30 capsules · 1 a day", "probiotics", None)
CREA = ("Creatine", "Mattisson Healthstyle", "Creatine Creapure® capsules", "180 vegicaps · 6 a day (3 g)", "creatine", None)
DISCOVERY = ("Monthly discovery", "Daily Stack", "A new product to try, picked by us", "1 product a month", None, None)
STACK_LIST = [
  dict(id="foundation", name="Foundation", price="€109", per="/ month · free shipping", badge="Most popular",
       tagline="The everyday basics, done right. 5 supplements + a monthly discovery.",
       items=[MULTI, OMEGA, MAG, VITC, FLORA, DISCOVERY],
       extras=["Weekly pill organizer (first box)", "Your daily schedule", "A \"why this brand\" card for every product"], cta="Subscribe to Foundation"),
  dict(id="her", name="Her", price="€129", per="/ month · free shipping", badge=None,
       tagline="Put together for women. 6 supplements.",
       items=[("Women's multivitamin", "Vitakruid", "Multi Dag Vrouw", "30 tablets · 1 a day", "multivitamin", None), OMEGA, MAG,
              ("Vitamin B12", "Solgar", "Methylcobalamin 1000 µg", "30 nuggets · 1 a day", "vitamin-b12", "solgar-b12"), VITC, FLORA],
       extras=["Pill organizer (first box)", "Your daily schedule", "A \"why this brand\" card for every product"], cta="Subscribe to Her Stack"),
  dict(id="energy", name="Energy", price="€129", per="/ month · free shipping", badge=None,
       tagline="For busy days and training days. 6 supplements.",
       items=[("Sport multivitamin", "Vitakruid", "Multi Dag Man Sport", "30 tablets · 1 a day", "multivitamin", None), OMEGA, MAG, CREA, VITC, FLORA],
       extras=["Shaker (first box)", "Pill organizer (first box)", "Training-day schedule"], cta="Subscribe to Energy Stack"),
  dict(id="winter", name="Winter", price="€109", per="one-time · free shipping", badge="Christmas gift",
       tagline="A 30-day winter plan. 5 supplements + 4 extras.",
       items=[VITC, MULTI, OMEGA, MAG, FLORA],
       extras=["Ginger-lemon tea", "Dutch honey", "Lip balm", "Gift card"], cta="Order the Winter Stack", note="Order before 15 December for delivery before Christmas."),
]
