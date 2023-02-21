from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def calc():
    return render_template('calc.html')


@app.route('/result', methods=['POST'])
def result():

    monthly_mortgage = request.form['mortg_monthly']
    monthly_wifi = request.form['wifi_monthly']
    power_monthly = request.form['power_monthly']
    hoa_monthly = request.form['hoa_monthly']
    water_sewage_monthly = request.form['water_sewage_monthly']
    other_monthly = request.form['other_monthly']
    nightly_rate = request.form['nightly_rate']

    mortg_monthly = float(monthly_mortgage)
    mortg_monthly_formatted = "${:,.2f}".format(mortg_monthly)
    
    wifi_monthly = float(monthly_wifi)
    wifi_monthly_formatted = "${:,.2f}".format(wifi_monthly)

    power_monthly = float(power_monthly)
    power_monthly_formatted = "${:,.2f}".format(power_monthly)

    hoa_monthly = float(hoa_monthly)
    hoa_monthly_formatted = "${:,.2f}".format(hoa_monthly)

    other_monthly = float(other_monthly)
    other_monthly_formatted = "${:,.2f}".format(other_monthly)

    water_sewage_monthly = float(water_sewage_monthly)
    water_sewage_monthly_formatted = "${:,.2f}".format(water_sewage_monthly)

    nightly_rate = float(nightly_rate)
    #cleaning_fee = float(cleaning_fee)
    
    #yearly cost of the property including utilities
    yearly = (mortg_monthly + hoa_monthly + wifi_monthly + power_monthly + water_sewage_monthly + other_monthly) * 12
    yearly_result = "${:,.2f}".format(yearly)

    #monthly cost of property including utilities
    monthly = yearly / 12
    monthly_res = "${:,.2f}".format(monthly)

    #break even nights
    break_even = yearly // nightly_rate


    #guest nightly price
    actual_rate = nightly_rate * 1.14
    actual = "${:,.2f}".format(actual_rate)

    #expected gross revenue
    gross_rev = nightly_rate * (12*21)
    gross_rev_formatted = "${:,.2f}".format(gross_rev)

    #expected net revenue
    net_rev = (gross_rev * 0.97) - yearly
    net_rev_formatted = "${:,.2f}".format(net_rev)

    #if guestS books 3-7 nigths take into account host 3% and guest 14%

    return render_template(
        'calc.html',
        other_monthly=other_monthly,
        other_monthly_formatted=other_monthly_formatted,
        water_sewage_monthly=water_sewage_monthly,
        water_sewage_monthly_formatted=water_sewage_monthly_formatted,
        mortg_monthly=mortg_monthly,
        mortg_monthly_formatted=mortg_monthly_formatted,
        wifi_monthly=wifi_monthly,
        wifi_monthly_formatted=wifi_monthly_formatted,
        power_monthly=power_monthly,
        power_monthly_formatted=power_monthly_formatted,
        hoa_monthly=hoa_monthly,
        hoa_monthly_formatted=hoa_monthly_formatted,
        yearly_result=yearly_result,
        monthly_res=monthly_res,
        break_even=break_even,
        nightly_rate=nightly_rate,
        actual=actual,
        gross_rev_formatted=gross_rev_formatted,
        net_rev_formatted=net_rev_formatted,
        calc_success=True
    )


if __name__ == '__main__':
    app.run()
