<template>
  <div class="bot">
    <p style="align-self: flex-start; font-size: 30px; margin-bottom: 0">
      Бот помощник
    </p>
    <p style="align-self: flex-start; font-size: 12px">
      Готов ответить на ваши вопросы
    </p>
    <div class="message-field">
      <div
        v-for="item in all_messages"
        :key="item"
        :class="'animate__animated animate__fadeIn ' + item.class"
      >
        <el-tag
          v-if="item.type_of_message == 'text'"
          :type="item.type"
          effect="dark"
          class="mess"
          round
        >
          <p>
            {{ item.text }}
          </p>
        </el-tag>
        <el-image
          v-if="item.type_of_message == 'img'"
          :src="item.text"
          class="bot-img"
          fit="cover"
        />
      </div>
    </div>

    <div class="input-field animate__animated animate__fadeIn">
      <div v-if="state === 'base'">
        <el-button
          v-for="button in buttons_base"
          :key="button.text"
          :type="button.type_label"
          text
          style="margin-left: 0"
          @click="base(button.text)"
          >{{ button.text }}</el-button
        >
      </div>

      <div v-else-if="state === 'methodic'">
        <el-button
          v-for="button in buttons_methodic"
          :key="button.text"
          :type="button.type_label"
          text
          style="margin-left: 0"
          @click="methodic(button.text)"
          >{{ button.text }}</el-button
        >
      </div>

      <div v-else-if="state === 'contacts'">
        <el-button
          v-for="button in buttons_contacts"
          :key="button.text"
          :type="button.type_label"
          text
          style="margin-left: 0"
          @click="contacts(button.text)"
          >{{ button.text }}</el-button
        >
      </div>

      <div v-else-if="state === 'contacts_get_phone'">
        <el-input
          v-model="contact_phone"
          placeholder="Введите номер"
          autosize
          type="textarea"
          size="large"
          :rows="2"
          style="width: 80%; margin-right: 10px"
          v-if="type_problem !== null"
        />
        <el-button
          :icon="Promotion"
          circle
          v-if="type_problem !== null"
          @click="send_contact_phone"
        />
      </div>

      <div v-else-if="state === 'terms'">
        <el-button
          v-for="button in buttons_terms"
          :key="button.text"
          :type="button.type_label"
          text
          style="margin-left: 0"
          @click="terms(button.text)"
          >{{ button.text }}</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { Promotion } from "@element-plus/icons-vue";
export default {
  name: "TelegramWebApp",
  data() {
    return {
      Promotion: Promotion,
      input_text: "",
      state: "base",
      all_messages: [],

      contact_phone: "",
      buttons_base: [
        { type_label: "warning", text: "Информация о методике" },
        { type_label: "warning", text: "О нас" },
        { type_label: "warning", text: "Контакты" },
        { type_label: "warning", text: "Стоимость" },
        { type_label: "warning", text: "Условия выполнения" },
      ],
      buttons_methodic: [
        { type_label: "warning", text: "Хочу записаться" },
        { type_label: "warning", text: "Подхожу ли я данной методике?" },
        {
          type_label: "warning",
          text: "Что из себя представляет эта методика?",
        },
        { type_label: "warning", text: "Стоит ли мне проходить методику?" },
        { type_label: "warning", text: "← Назад" },
      ],
      buttons_contacts: [
        { type_label: "warning", text: "Перейти в главное меню" },
        { type_label: "warning", text: "Консультация с оператором" },
        { type_label: "warning", text: "Номер телефона" },
        { type_label: "warning", text: "Почта" },
        { type_label: "warning", text: "Istagram" },
        { type_label: "warning", text: "Facebook" },
        { type_label: "warning", text: "Оставить свой телефон" },
        { type_label: "warning", text: "← Назад" },
      ],
      buttons_terms: [
        { type_label: "warning", text: "Что нужно для рабооты?" },
        { type_label: "warning", text: "Перейти в главное меню" },
        { type_label: "warning", text: "Посмотреть видео инструкцию" },
        { type_label: "warning", text: "← Назад" },
      ],
    };
  },
  methods: {
    base(text) {
      this.mes_user(text, 400, "text");
      switch (text) {
        case "Информация о методике":
          this.mes_bot("Что вы хотите узнать?", 1000, "text");
          this.state = "methodic";
          break;
        case "О нас":
          this.mes_bot(
            "Красивый текст про нас с карнтинкой снизу",
            800,
            "text"
          );
          this.mes_bot("/main_page/heart.jpg", 1400, "img");
          break;
        case "Контакты":
          this.mes_bot("Какие контакты вы хотите получить?", 1000, "text");
          this.state = "contacts";
          break;
        case "Стоимость":
          this.mes_bot("Красивый текст про стоимость", 800, "text");
          break;
        case "Условия выполнения":
          this.mes_bot("Что вы хотите?", 800, "text");
          this.state = "terms";
          break;
        default:
          console.log("Error");
      }
    },

    methodic(text) {
      this.mes_user(text, 400, "text");
      switch (text) {
        case "Хочу записаться":
          this.mes_bot("Какой-то заготовленный текст", 1000, "text");
          this.state = "methodic";
          break;
        case "Подхожу ли я данной методике?":
          this.mes_bot("Какой-то заготовленный текст", 1000, "text");
          this.state = "methodic";
          break;
        case "Что из себя представляет эта методика?":
          this.mes_bot("Какой-то заготовленный текст", 1000, "text");
          this.state = "methodic";
          break;
        case "Стоит ли мне проходить методику?":
          this.mes_bot("Какой-то заготовленный текст", 1000, "text");
          this.state = "methodic";
          break;
        default:
          this.mes_bot("Главное меню", 1000, "text");
          this.state = "base";
      }
    },

    contacts(text) {
      this.mes_user(text, 400, "text");
      switch (text) {
        case "Перейти в главное меню":
          this.mes_bot("http://192.168.1.82:8080", 1000, "text");
          this.state = "contacts";
          break;
        case "Консультация с оператором":
          this.mes_bot("Какой-то заготовленный текст", 1000, "text");
          this.state = "contacts";
          break;
        case "Номер телефона":
          this.mes_bot("Телефон: +7777777777", 1000, "text");
          this.state = "contacts";
          break;
        case "Почта":
          this.mes_bot("test@test.test", 1000, "text");
          this.state = "contacts";
          break;
        case "Istagram":
          this.mes_bot("@test_inst", 1000, "text");
          this.state = "contacts";
          break;
        case "Facebook":
          this.mes_bot("@test_fb", 1000, "text");
          this.state = "contacts";
          break;
        case "Оставить свой телефон":
          this.mes_bot("Введите номер телефона", 1000, "text");
          this.state = "contacts_get_phone";
          break;
        default:
          this.mes_bot("Главное меню", 1000, "text");
          this.state = "base";
      }
    },

    terms(text) {
      this.mes_user(text, 400, "text");
      switch (text) {
        case "Что нужно для рабооты?":
          this.mes_bot("Список того, что нужно", 1000, "text");
          this.state = "terms";
          break;
        case "Перейти в главное меню":
          this.mes_bot("http://192.168.1.82:8080", 1000, "text");
          this.state = "terms";
          break;
        case "Посмотреть видео инструкцию":
          this.mes_bot("ссылка на видео", 1000, "text");
          this.state = "terms";
          break;
        default:
          this.mes_bot("Главное меню", 1000, "text");
          this.state = "base";
      }
    },

    send_contact_phone() {
      this.mes_bot(this.contact_phone, 500, "text");
      this.mes_bot("Отправлено", 1000, "text");
      this.state = "base";
    },

    mes_user(text, timeout, type_of_message) {
      setTimeout(() => {
        this.all_messages = [
          {
            text: text,
            class: "mes-user",
            type: "success",
            type_of_message: type_of_message,
          },
        ].concat(this.all_messages);
      }, timeout);
    },

    mes_bot(text, timeout, type_of_message) {
      setTimeout(() => {
        this.all_messages = [
          {
            text: text,
            class: "mes-bot",
            type: "",
            type_of_message: type_of_message,
          },
        ].concat(this.all_messages);
      }, timeout);
    },
  },
  mounted() {
    this.mes_bot("Здравствуйте", 500, "text");
    this.mes_bot(
      "Выберите любой интерисующий вас вопрос - и я с удовольствием на него отвечу",
      1000,
      "text"
    );
    this.mes_bot("Выберите тематику вопроса:", 1500, "text");
  },
};
</script>

<style lang="scss">
.bot {
  width: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 10;

  .message-field {
    height: 50vh;
    display: flex;
    flex-direction: column-reverse;
    align-items: flex-end;
    margin-bottom: 10px;
    overflow: auto;

    .mess {
      height: 50px;

      margin-bottom: 0;
      margin: 10px;
      white-space: normal;
    }
    .bot-img {
      height: 150px;
      width: 150px;
    }
    .mes-user {
      align-self: flex-end;
      margin: 13px;
    }

    .mes-bot {
      align-self: flex-start;
      margin: 5px;
    }
  }

  .input-field {
    justify-content: center;
    align-items: center;
    width: 100%;
  }
}
</style>
