# Purnava (पुर्नवा)

Purnava (meaning "renewal" or "rebirth") is an impact-driven e-commerce platform designed to showcase and market handmade products crafted by incarcerated artisans across Nepal's correctional facilities. 

By bridging traditional prison craftsmanship with modern digital commerce, Purnava empowers inmates through financial independence, post-release capital, and dignified rehabilitation while offering customers high-quality, authentic products paired with transparent impact stories.

---

## Table of Contents
1. Key Features
2. The Social & Economic Context in Nepal
   - Quality and Reputation (Muda & Handcrafts)
   - Fact-Checking the Gulmi Prison Economy
3. Transformative Impact on Inmate Lives
4. Financial Architecture & Transparency Model
5. System Architecture & Relational Schema
6. Tech Stack
7. Getting Started (Backend & Database)
8. Project Folder Structure
9. Security, Privacy & Ethical Governance
10. License & Acknowledgments

---

## 1. Key Features

* **Impact Story Cards:** Every product is directly linked to an inmate artisan profile featuring their story, skill set, and rehabilitation goals.
* **Multi-Vault Automated Revenue Split:** Programmatically splits order proceeds into Inmate Savings, Workshop Material Funds, and Platform Operations upon payment verification.
* **Prison Admin Portal:** Tailored interface for prison welfare officers to list products, manage inventory, write story narratives, and audit earnings.
* **Digital Transparency Receipts:** Customers receive an itemized breakdown showing the exact financial allocation of their purchase.
* **Role-Based Security:** Strict access separation between Public Customers, Prison Administrators, and Super Administrators.

---

## 2. The Social & Economic Context in Nepal

### Quality and Reputation: *Muda* & Artisanship
In Nepal, products manufactured within correctional facilities carry a well-established reputation for high quality and durability:
* **Bamboo Stools (*Muda - मुडा*):** Prison-made *mudas* are widely regarded as the gold standard in Nepalese households due to tight hand-weaving techniques and sturdy structural framing compared to mass-produced market alternatives.
* **Textiles, Carpentry & Metalwork:** Inmates produce fine woolen garments, hand-carved furniture, traditional woven cotton fabrics, and decorative metal items.

### Fact-Checking the Gulmi Prison Economy
* **The Claim:** Popular narratives and local media discussions occasionally claim that smaller regional facilities, such as Gulmi District Prison, generate or export products worth up to **NPR 60 Crore (600 Million NPR)** annually.
* **Fact Check & Administrative Reality:**
  * **Scale Assessment:** Gulmi Prison is a modest facility housing approximately 100 to 120 inmates. An annual turnover of NPR 60 Crore would mean an average output exceeding **NPR 50 Lakhs per inmate per year**, which is far above the realistic physical and logistical capacity of a small prison workshop.
  * **Official Data:** Department of Prison Management (DoPM) reports indicate that total annual product sales across smaller district prisons typically range between **NPR 15 Lakhs and 1 Crore**, whereas major central facilities (e.g., Central Jail Sundhara, Pokhara Prison) handle multi-crore operations.
  * **Core Conclusion:** While the "60 Crore" figure is an exaggerated rumor, the underlying fact remains valid: **District prisons in Nepal host highly active micro-economies** where artisan labor generates meaningful revenue and self-reliance.

---

## 3. Transformative Impact on Inmate Lives

1. **Financial Support for Families:** Inmates can remit earnings directly to their families on the outside to fund living expenses, children's education, and medical needs.
2. **Post-Release Savings Vault:** A substantial portion of earnings is locked in an institutional trust account released upon completion of their sentence, preventing re-offending caused by immediate post-release poverty.
3. **Mental Well-being & Rehabilitation:** Engaging in skilled craft work provides therapeutic focus, reduces institutional stress, and restores a sense of pride and purpose.
4. **Market-Ready Vocational Skills:** Hands-on experience in woodworking, weaving, and production management equips inmates with sustainable trades for reintegration into society.

---

## 4. Financial Architecture & Transparency Model

Purnava uses an automated revenue-sharing formula for every item sold:

```
                      +-----------------------------+
                      |   Customer Order Payment    |
                      +-----------------------------+
                                     |
           +-------------------------+-------------------------+
           |                         |                         |
           v                         v                         v
  [ Prisoner Trust Vault ]  [ Material & Workshop ]  [ Purnava Operations ]
          (45%)                     (35%)                     (20%)
           |                         |                         |
           v                         v                         v
  Held in official trust    Reinvested in raw tools,   Covers shipping, web
  for post-release fund     bamboo, wood & dyes       hosting & gateway fees
  or family remittance      for continuous production  
```

---

## 5. System Architecture & Relational Schema

```
[ Facility ] 
     │
     ├─── (1 : Many) ───> [ Prison Admin (User) ]
     │
     └─── (1 : Many) ───> [ Prisoner ] 
                             │
                             ├─── (1 : 1) ─────────> [ Impact Story Card ]
                             │
                             └─── (1 : Many) ──────> [ Product ]
                                                        │
                                                        └─── (1 : Many) ───> [ Order Item ]
                                                                                  │
                                                                                  └─── (1 : 1) ───> [ Payout Ledger ]
```

---

## 6. Tech Stack

* **Backend Engine:** FastAPI (Python 3.11+)
* **Database Management:** PostgreSQL + SQLAlchemy 2.0 (Async Mappings)
* **Data Validation:** Pydantic v2
* **Migrations:** Alembic
* **Frontend UI (Planned):** Next.js / React (TypeScript) + Tailwind CSS

---

## 7. Getting Started (Backend & Database)

### Prerequisites
* Python 3.11 or higher
* PostgreSQL database instance

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/purnava.git
   cd purnava
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the project root directory:
   ```env
   DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/purnava_db
   SECRET_KEY=your_super_secret_jwt_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

5. **Run Database Migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Launch Development Server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   Open `http://127.0.0.1:8000/docs` in your browser to view the interactive API documentation.

---

## 8. Project Folder Structure

```
purnava/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization & middleware
│   ├── config.py            # Environment settings and configuration
│   ├── database.py          # Async SQLAlchemy engine & session factory
│   ├── models/              # SQLAlchemy 2.0 DB models
│   │   ├── __init__.py
│   │   ├── facility.py
│   │   ├── user.py
│   │   ├── prisoner.py
│   │   ├── product.py
│   │   └── order.py
│   ├── schemas/             # Pydantic v2 validation schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   ├── routers/             # FastAPI route handlers
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── stories.py
│   │   └── orders.py
│   └── services/            # Business logic (e.g., payout split calculations)
├── alembic/                 # Database migration scripts
├── tests/                   # Pytest test suite
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 9. Security, Privacy & Ethical Governance

* **Anonymity & Protection:** To comply with legal guidelines and respect individual rights, real names and faces of incarcerated persons are never displayed publicly without formal consent. Inmates are represented by public display codes (e.g., *Artisan #402*).
* **Auditability:** Payout Ledgers are immutably tied to order receipts, allowing welfare officers and auditors to verify that every allocated rupee reaches the designated trust account.

---

## 10. License & Acknowledgments

This project is licensed under the MIT License. Special acknowledgment to the correctional facility welfare officers and artisan communities working towards rehabilitation through craftsmanship in Nepal.
